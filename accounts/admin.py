from django.contrib import admin
from .models import *
# Register your models here.
class MyUserAdmin(admin.ModelAdmin) :
    list_display = ['id','email','role']

admin.site.register(MyUser,MyUserAdmin)

