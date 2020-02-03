from django.shortcuts import render,get_object_or_404,redirect
from parlour.forms import AppoinmentForm
from parlour.models import *
from adminsection.models import Service
from django.urls import reverse



def home(request):

    """
        Provides the ability to make an appoinment via user
    """
    services = Service.objects.all()
    form     = AppoinmentForm(request.POST or None)
      
    if request.method=='POST':
       
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            form.save_m2m()
         
            return redirect(reverse("thankyou", kwargs={
                'id': form.instance.id
            }))

    context={
 
            'form':form,
            'services':services,
            }
    return render(request,'website/index.html',context)


def services(request):
    """
        Listing Page for Services
    """
    services = Service.objects.all()
    context={
        
            'services':services,
    }
    return render(request,'website/services.html',context)


def about(request):
    """
        About Page
    """  
    return render(request,'website/about.html')


def contact(request):
    """
        About Page
    """  
    return render(request,'website/contact.html')

def thankyou(request,id):
    """
        Thankyou Page. Redirect here after customers make their appointment & get their appointmentnumber
    """      
    appoinmentid = get_object_or_404(Appoinment,id=id)
    return render(request,'website/thankyou.html',{'appoinment':appoinmentid})
