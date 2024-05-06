from django.contrib import admin
from .models import Admin, Guest, Token

# Register your models here.
admin.site.register(Admin)
admin.site.register(Guest)
admin.site.register(Token)
