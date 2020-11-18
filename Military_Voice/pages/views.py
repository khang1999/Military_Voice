from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from text_prompts.models import Sentence
import wave

from text_prompts.serializers import SentenceSerializer

from audio_recordings.models import Recording
from audio_recordings.serializers import RecordingSerializer
from json import dumps

# Create your views here.

class FrontendRenderView(View):
    def get(self, request, *args, **kwargs):
        sentences = Sentence.objects.all()
        serializers = SentenceSerializer(sentences, many = True)
        recordings = Recording.objects.all()
        recordingSerializer = RecordingSerializer(recordings, many = True)
        data = {'data': JsonResponse(serializers.data, safe = False).content.decode(),
				'audio_data': JsonResponse(recordingSerializer.data, safe=False).content.decode()}

        return render(request, "pages/front-end-render.html", data)

@method_decorator(csrf_exempt, name='dispatch')
class SpeakView(View):
	def get(self, request, *args, **kwargs):
		sentences = Sentence.objects.all()
		serializers = SentenceSerializer(sentences, many = True)

		recordings = Recording.objects.all()
		recordingSerializer = RecordingSerializer(recordings, many = True)

		data = {'data': JsonResponse(serializers.data, safe = False).content.decode(),
				'audio_data': JsonResponse(recordingSerializer.data, safe=False).content.decode()}

		return render(request, "pages/speak.html", data)

	def post(self, request, *args, **kwargs):
		#recordings = Recordings.objects.update_or_create(
		print(request.POST['verified'])
		message = "Post Failed"
		if(request.POST['verified'] == '0'):
			print("this is running")
			filename = request.POST['filename']
			textid = request.POST['textid']
			text = request.POST['text']
			audiofile = request.FILES['audiofile']
			verified = request.POST['verified']
			#)

			recordings = Recording.objects.update_or_create(
				fileName = filename,
				textid = textid,
				text = text,
				audiofile = filename,
				verified = verified
			)

			def save_to_tmp_folder(form_data, source_file_name):
			    with open('media/' + source_file_name, 'wb+') as destination:
			        for chunk in form_data.chunks():
			            destination.write(chunk)
			print(recordings)

			save_to_tmp_folder(audiofile, filename)
			message = "upload successful"

		elif(request.POST['verified'] == '1'):
			print(request.POST['id'])
			audiofile = Recording.objects.get(pk=request.POST['id'])
			audiofile.verified = request.POST['verified']
			audiofile.save()

			message = "verification successful"

		elif(request.POST['verified'] == '2'):
			print(request.POST['id'])
			audiofile = Recording.objects.get(pk=request.POST['id'])
			audiofile.delete()

			message = "delete successful"
		#print(request.body)
		

		# recordings = Recordings.objects.get()
		# recordings.fileName = request.POST['fileName']
		# recordings.audiofile = request.POST['audiofile']
		# recordings.textid = request.POST['textid']
		# recordings.text = request.POST['text']

		#print(recordings)

		# recordings.save()

		return HttpResponse(message)

class DatasetsView(View):
    def get(self, request, *args, **kwargs):
        sentences = Sentence.objects.all()
        serializers = SentenceSerializer(sentences, many = True)
        recordings = Recording.objects.all()
        recordingSerializer = RecordingSerializer(recordings, many = True)
        data = {'data': JsonResponse(serializers.data, safe = False).content.decode(),
				'audio_data': JsonResponse(recordingSerializer.data, safe=False).content.decode()}
        return render(request, "pages/datasets.html", data