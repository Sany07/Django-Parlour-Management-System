from django.contrib import admin
from .models import *
# Register your models here.



class MyModelAdmin(admin.ModelAdmin):
    
    readonly_fields  = ['ApplyDate','RemarkDate']

admin.site.register(Appoinment , MyModelAdmin)  

