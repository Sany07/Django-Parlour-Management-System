from django.shortcuts import render,get_object_or_404,redirect
from adminsection.forms import *
from adminsection.models import *
from django.contrib import auth
from django.urls import reverse

from parlour.models import Appoinment

# Create your views here.


def signin(request):

    form     = LoginForm(request.POST or None)

    if request.user.is_authenticated:
        return redirect('dashboard')
    
    else:
        
        if request.method=='POST':
            if form.is_valid():
                auth.login(request, form.get_user())
                return redirect('dashboard')
    context={
            'form':form, 
    }
    return render(request,'adminsection/signin.html',context)



def dashboard(request):
    return render(request,'adminsection/dashboard.html')
    

    
def addcustomer(request):

    form     = AddCustomerForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            

    context={
            'form':form
        }
    return render(request,'adminsection/add-customer.html',context)


def addservice(request):

    form     = AddServiceForm(request.POST or None)
    
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('manageservices')
    context={
            'form':form
        }
    
    return render(request,'adminsection/add-services.html',context)

def manageservices(request):


    Services=Service.objects.order_by('-TimeStamp')

    context={
            'Services':Services
        }
    return render(request,'adminsection/manage-services.html',context)  



def updateservice(request,id):
    
    service=get_object_or_404(Service,id=id)
    form     = AddServiceForm(request.POST or None , instance=service)
 
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('manageservices')

    context={
        'form':form
    }
    return render(request,'adminsection/edit-services.html',context)

def customerlist(request):
    return render(request,'adminsection/customer-list.html')
    
def bwdatesreportsds(request):
    return render(request,'adminsection/bwdates-reports-ds.html')
    
def salesreports(request):
    return render(request,'adminsection/sales-reports.html')
    
   
def allappointment(request):
    Appoinments = Appoinment.objects.order_by('-ApplyDate')
    context={
        'Appoinments':Appoinments
    }
    return render(request,'adminsection/all-appointment.html',context)

def viewappointment(request,id):
    
    Appoinments=get_object_or_404(Appoinment,id=id)
    context={
        'Appoinment':Appoinments
    }
    return render(request,'adminsection/view-appointment.html',context)

    
def newappointment(request):
    return render(request,'adminsection/new-appointment.html')
    
def acceptedappointment(request):
    return render(request,'adminsection/accepted-appointment.html')
    
def invoices(request):
    return render(request,'adminsection/invoices.html')
    
def searchappointment(request):
    return render(request,'adminsection/search-appointment.html')
    
def searchinvoices(request):
    return render(request,'adminsection/search-invoices.html')
    


# def dashboard(request):
#     return render(request,'adminsection/dashboard.html')
    
# def dashboard(request):
#     return render(request,'adminsection/dashboard.html')
    
