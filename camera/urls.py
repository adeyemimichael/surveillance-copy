from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('dashboard/admin', views.admin, name = 'admin'),
    path('dashboard/guest', views.guest, name = 'guest')
]