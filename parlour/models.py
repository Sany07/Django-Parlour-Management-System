from django.db import models
import uuid

# Create your models here.

class Appoinment(models.Model):


    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=11)
    Service = models.CharField(max_length=50)
    Note = models.TextField()
    AppoinmentDate = models.DateField()
    AppoinmentTine = models.TimeField()  
    ApplyDate = models.DateTimeField(auto_now_add=True)
    RemarkDate = models.DateTimeField(auto_now=True)
    REMARK_CHOICES = (
        ('1', 'Accepted'),
        ('0', 'Rejected'),
    )
    Remark = models.CharField(max_length=1, choices=REMARK_CHOICES)
    def __str__(self):
        return self.Name


