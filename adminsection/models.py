from django.db import models

# Create your models here.
class Service(models.Model):
    ServiceName = models.CharField(max_length=25)
    Cost = models.PositiveIntegerField()
    TimeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ServiceName
        
class Customer(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=11)
    GENDER_CHOICES = (
        ('0', 'Male'),
        ('1', 'Female'),
    )
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
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