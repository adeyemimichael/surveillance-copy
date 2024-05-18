from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from camera.views import guest, admin, index
from datetime import datetime

# Create your views here.
def admin_login(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      our_user = User.objects.get(username=username)

      user = auth.authenticate(username=username, password=password)
      if user is not None:
         if Admin.objects.filter(user=our_user).exists():
            auth.login(request, user)
            return redirect('admin')
         else:
            messages.info(request, 'You do not have Admin priviledge')
            return redirect('admin_login')
      else:
         messages.info(request, 'incorrect username or password')
         return redirect('admin_login')
      
   return render(request, 'admin/login.html')
   

def admin_reg(request):
   if request.method == "POST":

      username = request.POST.get('username')
      password = request.POST.get('password')
      confirm_password = request.POST.get('confirm_password')
      token = request.POST.get('token')

      a_token = Token.objects.get(id=1)

      if User.objects.filter(username=username).exists():
         messages.info(request, 'username already taken')
         return redirect('admin_reg')
    
      else:
         if password == confirm_password:
            if token == a_token.token:
               user = User.objects.create_user(username=username, password=password)
               user.save()
               admin = Admin(user=user, token=a_token.token, created_at=datetime.now())
               admin.save()
               messages.info(request, "user created successfully")
               return redirect('admin_login')
         
            else:
               messages.info(request, "Please get a valid token")
               return redirect('admin_reg')
            
         else:
            messages.info(request, "password does not match")
            return redirect('admin_reg')
      
   return render(request, 'admin/register.html')


def admin_logout(request):
   auth.logout(request)
   return redirect('index')


def guest_login(request):
   if request.method == 'POST':

      username = request.POST.get('username')
      password = request.POST.get('password')

      our_user = User.objects.get(username=username)
      user = auth.authenticate(username=username, password=password)

      guest = Guest.objects.get(user=our_user)

      if user is not None:
         if guest.is_authorized:
            auth.login(request, user)
            return redirect('guest')
         else:
            messages.info(request, 'you are not authorized')
      else:
         messages.info(request, 'incorrect username or password')
         return redirect('guest_login')

   return render(request, 'guest/login.html')


def guest_reg(request):
   if request.method == "POST":

      username = request.POST.get('username')
      password = request.POST.get('password')
      confirm_password = request.POST.get('confirm_password')

      if User.objects.filter(username=username).exists():
         messages.info(request, "username already taken")
         return redirect('guest_reg')
    
      else:
         if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            guest = Guest(user=user, created_at=datetime.now(), is_authorized=True)
            guest.save()
            messages.info(request, 'user created successfully')
            return redirect('guest_login')
            
         else:
            messages.info(request, "password does not match")
            return redirect('guest_reg')
         
   return render(request, 'guest/register.html')

def guest_logout(request):
   auth.logout(request)
   return redirect('index')
