from django.db import models
import uuid

# Create your models here.

class Appoinment(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=11)
    Service = models.CharField(max_length=50)
    Note = models.TextField()
    Remark = models.BooleanField(default=False)
    AppoinmentDate = models.DateField(default=None)
    AppoinmentTine = models.TimeField()  
    ApplyDate = models.DateTimeField(auto_now_add=True)
    RemarkDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name


