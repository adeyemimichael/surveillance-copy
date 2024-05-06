from django.urls import path
from . import views


urlpatterns = [
    path('admin/register', views.admin_reg, name = 'admin_reg'),
    path('admin/login', views.admin_login, name = 'admin_login'),
    path('admin/logout', views.admin_logout, name = 'admin_logout'),
    path('guest/register', views.guest_reg, name = 'guest_reg'),
    path('guest/login', views.guest_login, name = 'guest_login'),
    path('guest/logout', views.guest_logout, name = 'guest_logout'),
]