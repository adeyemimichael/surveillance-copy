from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('dashboard/admin', views.admin, name = 'admin'),
    path('dashboard/guest', views.guest, name = 'guest'),
    path('dashboard/webcam', views.webcam, name = 'webcam'),
    # path('start_recording/', views.start_recording, name='start_recording'),
    # path('stop_recording/', views.stop_recording, name='stop_recording'),
    path('recordings/', views.recordings, name='recordings'),
    path('play_recording/<int:recording_id>/', views.play_recording, name='play_recording'),

]