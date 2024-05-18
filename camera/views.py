from django.shortcuts import render, redirect
from django.http.response import StreamingHttpResponse, HttpResponse
from camera.cam import IpWebCam
from .models import Recording
import os

camera = IpWebCam("http://192.168.112.205:8080/shot.jpg")


# Create your views here.
def index(request):
   return render(request, 'camera/index.html')

def admin(request):
   recordings = Recording.objects.all()
   return render(request, 'camera/admin_dashboard.html', {'recordings': recordings})

def guest(request):
   return render(request, 'camera/guest_dashboard.html')

def gen(cam):
   while True:
      frame = cam.get_frame()
      yield (b'--frame\r\n'
             b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def webcam(request):
   return StreamingHttpResponse(gen(camera),
                                content_type='multipart/x-mixed-replace; boundary=frame')
# def start_recording(request):
#     camera.start_recording()
#     return redirect('admin')

# def stop_recording(request):
#     filepath = camera.stop_recording()
#     Recording.objects.create(file_path=filepath)
#     return redirect('admin')

def recordings(request):
    recordings = Recording.objects.all()
    return render(request, 'camera/recordings.html', {'recordings': recordings})

def play_recording(request, recording_id):
    recording = Recording.objects.get(id=recording_id)
    file_path = recording.file_path
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type="video/avi")
        response['Content-Disposition'] = f'inline; filename={os.path.basename(file_path)}'
        return response