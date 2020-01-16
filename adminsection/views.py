from django.shortcuts import render,get_object_or_404,redirect
from adminsection.forms import LoginForm
from django.contrib import auth
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
    

    