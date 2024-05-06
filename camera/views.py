from django.shortcuts import render


# Create your views here.
def index(request):
   return render(request, 'camera/index.html')

def admin(request):
   return render(request, 'camera/admin_dashboard.html')

def guest(request):
   return render(request, 'camera/guest_dashboard.html')
