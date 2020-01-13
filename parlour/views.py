from django.shortcuts import render
from parlour.forms import AppoinmentForm
from parlour.models import *

# Create your views here.


def home(request):
    services = Service.objects.all()
    form     = AppoinmentForm(request.POST or None)
    
    
    print(form)
    if request.method=='POST':
        if form.is_valid():
            
            instance=form.save(commit=False)

            instance.save()
        
        #    answer = form.cleaned_data.get('filter_by') 
           
        #     return redirect(reverse("post" ,kwargs={
        #         'id':form.instance.id
        # }))

    context={
            
               
            'form':form,
            'services':services,
            

                
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

# # def home(request):
# #     return render(request,'index.html')



    

#     s=Invoice.objects.all()
#     qs=Test.objects.all()
#     c=Customers.objects.all()

# # entry = Entry.objects.get(pk=1)
# # >>> cheese_blog = Blog.objects.get(name="Cheddar Talk")
# # >>> entry.blog = cheese_blog
# # >>> entry.save()

#     if request.method=='POST':
#         p= request.POST['title']
#         c= request.POST['name']
#         cs= request.POST.getlist('cat')  

#         a=int(c)
#         print(type(a))

#         a1=Invoice(note=p)
        
#         a1.customer=a
#         a1.save()
        
#         for i in cs:
#             a1.catagories.add(i)
        
#         # users = Catagory.objects.filter(title=cs)
#         # instance = Selector.objects.create(title=title)

#         # instance.catagories.set(users)
#     context={
            
#                 'qs':qs,
#                 's':s,
#                 'c':c,

                
#             }
#     return render(request,'index.html',context)

# def home(request):
#     form=AppoinmentForm(request.POST or None)
#     if request.method=='POST':
#         p= request.POST['title']
#         c= request.POST['name']
#         c= request.POST['name']

#         cs= request.POST.getlist('cat')  

#         a=int(c)
#         print(type(a))

#         a1=Invoice(note=p)
        
#         a1.customer=a
#         a1.save()
        
#         for i in cs:
#             a1.catagories.add(i)
        
#     context={
            
               
#             'form':form
            

                
#             }
#     return render(request,'index.html',context)