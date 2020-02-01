from django.shortcuts import render,get_object_or_404,redirect
from adminsection.forms import *
from adminsection.models import *
from parlour.models import Appoinment
from django.contrib import auth
from django.urls import reverse
from django.db.models import Q
from django.db.models import Sum
from datetime import date , timedelta

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

    total_appoinment = Appoinment.objects.all().count()
    total_accepted_appoinment = Appoinment.objects.filter(Remark = 1).count()
    total_Rejected_appoinment = Appoinment.objects.filter(Remark = 0).count()
    total_service = Service.objects.all().count()
    total_customer = Customer.objects.all().count()
    total_sales = Invoice.objects.values('Catagories__Cost').aggregate(Sum('Catagories__Cost'))
    today_sales = Invoice.objects.filter(Date__date=date.today()).aggregate(Sum('Catagories__Cost'))
    yesterday_sales = Invoice.objects.filter(Date__date=date.today()- timedelta(days=1)).aggregate(Sum('Catagories__Cost'))
    last_seven_days_sales = Invoice.objects.filter(Date__gte=date.today()- timedelta(days=7)).aggregate(Sum('Catagories__Cost'))


    context={
            'total_appoinment':total_appoinment,
            'total_accepted_appoinment':total_accepted_appoinment,
            'total_Rejected_appoinment':total_Rejected_appoinment,
            'total_service':total_service,
            'total_customer':total_customer,
            'total_sales':total_sales,
            'today_sales':today_sales,
            'yesterday_sales':yesterday_sales,
            'last_seven_days_sales':last_seven_days_sales
            
        }
    return render(request,'adminsection/dashboard.html',context)
    

    
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
    Services=Service.objects.order_by('-TimeStamp')

    if request.method=='POST':
        # total_price=request.POST['total_price']
        # discount_price=request.POST['discount_price']
        serviceid= request.POST.getlist('serviceid')
        
        # if discount_price:
        #     final_price=int(total_price)-int(discount_price)  
        #     a1=Invoice(Note=final_price)
            
        # else:
        #     a1=Invoice()

        a1=Invoice()   
        a1.Customer=customer
        a1.save()
        for obj in serviceid:
            a1.Catagories.add(obj)
                
        return redirect('invoices')    
    context={
            'Services':Services ,
            'customer':customer
        }

    return render(request,'adminsection/add-customer-services.html',context)
 

    
   
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

    invoices = Invoice.objects.order_by('-id')

    context={
        'invoices':invoices
    }
    return render(request,'adminsection/invoices.html',context)


def viewinvoice(request,id):
    invoice = get_object_or_404(Invoice,id=id)
    total = Invoice.objects.filter(id=id).aggregate(Sum('Catagories__Cost'))

    
    context={
        'invoice':invoice ,
        'total':total
    }
    return render(request,'adminsection/view-invoice.html',context)


def searchappointment(request):
    appointment_list=''
    query= request.GET.get('searchdata')
    if query:
        appointment_list=Appoinment.objects.all()
        appointment_list= appointment_list.filter(
            Q(AppointmentNumber__iexact=query) |
            Q(Name__icontains=query) |
            Q(Email__iexact=query)
        ).distinct()
     
    context={

            'appointment_list':appointment_list,
            'query':query
        }

    
    return render(request,'adminsection/search-appointment.html',context)
    
def searchinvoices(request):

    query= request.GET.get('searchdata')

    invoice =Invoice.objects.filter(BillingNumber=query)

    context={
        'invoice':invoice,
        'query':query
    }
    return render(request,'adminsection/search-invoices.html',context)
    


def bwdatesreportsds(request):

    
    invoice_list=''
    from_date= request.GET.get('from_date')
    to_date= request.GET.get('to_date')



    if from_date and to_date:

        invoice_list =Invoice.objects.all() 
        
        invoice_list= invoice_list.filter(
            Q(Date__gte=from_date),
            Q(Date__lte=to_date)
        ).distinct()

    context={

        'invoice_list':invoice_list,
        'from_date':from_date,
        'to_date':to_date
    }

    return render(request,'adminsection/bwdates-reports-ds.html',context)
    
def salesreports(request):
    return render(request,'adminsection/sales-reports.html')

def profile(request):
    return render(request,'adminsection/admin-profile.html')
    
def changepassword(request):
    return render(request,'adminsection/change-password.html')

def forgetpassword(request):
    return render(request,'adminsection/forget-password.html')
     
def contactus(request):
    return render(request,'adminsection/contact-us.html')

def logout(request):
    pass
    
    