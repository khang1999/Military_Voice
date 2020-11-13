from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Sentence
from .serializers import SentenceSerializer
from django.views.decorators.csrf import csrf_exempt

import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

# Create your views here.


@csrf_exempt
def sentence_list(request):
	if request.method == 'GET':
		sentences = Sentence.objects.all()
		serializers = SentenceSerializer(sentences, many = True)


		return JsonResponse(serializers.data, safe = False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = SentenceSerializer(data=data)

		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status = 201)
		return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def sentence_detail(request, pk):
	try:
		sentence = Sentence.objects.get(pk=pk)

	except Sentence.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = SentenceSerializer(sentence)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = SentenceSerializer(sentence, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status = 400)

	elif request.method == 'DELETE':
		sentence.delete()
		return HttpResponse(status = 204)



@permission_required('admin.can_add_log_entry')
def sentence_upload(request):
	template = "sentence_upload.html"

	prompt = {
		'order': 'Order of the CSV should be sentence, count'
	}

	if request.method == "GET":
		return render(request, template, prompt)

	csv_file = request.FILES['file']

	if not csv_file.name.endswith('.csv'):
		message.error(request, 'This is not a csv file')

	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)

	next(io_string)
	for column in csv.reader(io_string, delimiter = ','): 
		_, created = Sentence.objects.update_or_create(
				text=column[0],
				count=column[1]
			)

	context = {}

	return render(request, template, context)