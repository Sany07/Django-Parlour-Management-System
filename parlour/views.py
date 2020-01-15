from django.shortcuts import render,get_object_or_404,redirect
from parlour.forms import AppoinmentForm
from parlour.models import *
from adminsection.models import *

from django.urls import reverse
# Create your views here.


def home(request):

    """
        Provides the ability to make an appoinment via user
    """
    services = Service.objects.all()
    form     = AppoinmentForm(request.POST or None)
    s = Appoinment.objects.all()
    
  
    if request.method=='POST':
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            return redirect(reverse("thankyou" ,kwargs={
                'id':form.instance.id
        }))
    context={
 
            'form':form,
            'services':services,
            's':s
            }
    return render(request,'index.html',context)




def services(request):
    services = Service.objects.all()
    context={
        
            'services':services,
    }
    return render(request,'services.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def thankyou(request,id):

    appoinmentid = get_object_or_404(Appoinment,id=id)
    return render(request,'thankyou.html',{'appoinment':appoinmentid})