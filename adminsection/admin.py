from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Customer)
admin.site.register(Invoice)
class MyModelAdmin(admin.ModelAdmin):
    
    readonly_fields  = ['TimeStamp']

admin.site.register(Service , MyModelAdmin)  
