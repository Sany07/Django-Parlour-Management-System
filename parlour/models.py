from django.db import models
import uuid

# Create your models here.
class Service(models.Model):
    ServiceName = models.CharField(max_length=25)
    Cost = models.PositiveIntegerField()

    def __str__(self):
        return self.ServiceName


class Appoinment(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=11)
    Services = models.CharField(max_length=50)
    Note = models.TextField()
    Remark = models.BooleanField(default=False)
    AppoinmentDate = models.DateField(default=None)
    AppoinmentTine = models.TimeField()  
    ApplyDate = models.DateTimeField(auto_now_add=True)
    RemarkDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name



class Customer(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=11)
    Gender = models.CharField(max_length=11)
    Note = models.TextField()
    CreateDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Name           

class Invoice(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Catagories = models.ManyToManyField(Service)
    Date = models.DateTimeField(auto_now_add=True)
    Note= models.TextField()
    
    def __str__(self):
        return self.id

