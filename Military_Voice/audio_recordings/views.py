from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Recording
from .serializers import RecordingSerializer
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import csv, io, zipfile, os
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
# Create your views here.


@csrf_exempt
def recordings_list(request):
	if request.method == 'GET':
		recordings = Recording.objects.all()
		serializers = RecordingSerializer(recordings, many = True)

		return JsonResponse(serializers.data, safe = False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = RecordingSerializer(data=data)

		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status = 201)
		return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def recordings_detail(request, pk):
	try:
		recordings = Recording.objects.get(pk=pk)

	except Recordings.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = RecordingSerializer(sentence)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = SentenceSerializer(sentence, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status = 400)

	elif request.method == 'DELETE':
		recordings.delete()
		return HttpResponse(status = 204)

@permission_required('admin.can_log_entry')
def recordings_download(request):
	items = Recording.objects.all()
	response = HttpResponse(content_type = 'text/csv')

	response['Content-Disposition'] = 'attachment: filename="recordings.csv"'

	writer = csv.writer(response, delimiter=',')
	writer.writerow(['file_name', 'text'])

	for obj in items:
		writer.writerow([obj.fileName, obj.text])

	return response

@permission_required('admin.can_log_entry')
def recordings_audio_download(request):
	response = HttpResponse(content_type='application/zip')
	zip_file = zipfile.ZipFile(response, 'w')
	context_dict = {}
	files = os.listdir(os.path.join(settings.MEDIA_ROOT, ""))
	context_dict['files'] = files
	for filename in files:
		zip_file.write("media/" + filename)
	zip_file.close()
	# return render(request, 'datasets.html', context=context_dict)
	response['Content-Disposition'] = 'attachment; filename={}'.format("audio.zip")
	return response


