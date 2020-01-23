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



def addcustomer(request):

    form     = AddCustomerForm(request.POST or None)

    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('customerlist')
    context={
 
            'form':form,
            }
    return render(request,'adminsection/add-customer.html',context)


def customerlist(request):

    CustomerList = Customer.objects.order_by('-CreateDate')

    context={
        'CustomerList':CustomerList
    }
    return render(request,'adminsection/customer-list.html',context)

def editcustomer(request,id):
    
    customer=get_object_or_404(Customer,id=id)
    form     = AddCustomerForm(request.POST or None , instance=customer)
 
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('customerlist')

    context={
        'form':form
    }
    return render(request,'adminsection/edit-customer-detailed.html',context)

def assignservices(request , id):
    
    customer=get_object_or_404(Customer,id=id)
    # customer=Customer.objects.values('id').get(id=id)
    Services=Service.objects.order_by('-TimeStamp')
    if request.method=='POST':

        cs= request.POST.getlist('serviceid')  

        
        a1=Invoice(Note="hello")
        
        a1.Customer=customer
        a1.save()
        for i in cs:
            a1.Catagories.add(i)
    context={
            'Services':Services ,
            'customer':customer
        }

    return render(request,'adminsection/add-customer-services.html',context)
 
   
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
    form     = AppoinmentUpdateForm(request.POST or None , instance=Appoinments)
    
    if request.method=='POST':
        if form.is_valid():
            form.save()
            # return redirect('manageservices')
    context={
        'Appoinment':Appoinments,
        'form':form
    }
    return render(request,'adminsection/view-appointment.html',context)

    
def newappointment(request):

    Acceptedappoinments = Appoinment.objects.filter(Remark='')
    context={
        'Acceptedappoinments':Acceptedappoinments,
    }
    return render(request,'adminsection/new-appointment.html',context)
    
def acceptedappointment(request):

    Acceptedappoinments = Appoinment.objects.filter(Remark=1)

    context={
        'Acceptedappoinments':Acceptedappoinments,
    }
    return render(request,'adminsection/accepted-appointment.html',context)

def rejectedappointment(request):
    Rejectedtedappoinments = Appoinment.objects.filter(Remark=0)

    context={
        'Rejectedtedappoinments':Rejectedtedappoinments,
    }
    return render(request,'adminsection/rejected-appointment.html',context)   

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
    
