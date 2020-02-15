from django.shortcuts import render, get_object_or_404, redirect
from adminsection.forms import *
from adminsection.models import *
from parlour.models import Appoinment
from django.contrib import auth
from django.urls import reverse
from django.db.models import Q
from django.db.models import Sum
from datetime import date, timedelta
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.admin.views.decorators import staff_member_required


def signin(request):
    """
        LogIn page for Admin/Staff
    """ 
    form = LoginForm(request.POST or None)

    if request.user.is_authenticated:
        return redirect('dashboard')

    else:

        if request.method == 'POST':
            if form.is_valid():
                auth.login(request, form.get_user())
                return redirect('dashboard')
    context = {
        'form': form,
    }
    return render(request, 'adminsection/signin.html', context)


@staff_member_required
def dashboard(request):
    """
        Adminsection Dashboard.
    """ 
    total_appoinment = Appoinment.objects.all().count()
    total_accepted_appoinment = Appoinment.objects.filter(Remark=1).count()
    total_Rejected_appoinment = Appoinment.objects.filter(Remark=0).count()
    total_service = Service.objects.all().count()
    total_customer = Customer.objects.all().count()
    total_sales = Invoice.objects.values(
        'Catagories__Cost').aggregate(Sum('Catagories__Cost'))
    today_sales = Invoice.objects.filter(
        Date__date=date.today()).aggregate(Sum('Catagories__Cost'))
    yesterday_sales = Invoice.objects.filter(
        Date__date=date.today() - timedelta(days=1)).aggregate(Sum('Catagories__Cost'))
    last_seven_days_sales = Invoice.objects.filter(
        Date__gte=date.today() - timedelta(days=7)).aggregate(Sum('Catagories__Cost'))

    context = {
        'total_appoinment': total_appoinment,
        'total_accepted_appoinment': total_accepted_appoinment,
        'total_Rejected_appoinment': total_Rejected_appoinment,
        'total_service': total_service,
        'total_customer': total_customer,
        'total_sales': total_sales,
        'today_sales': today_sales,
        'yesterday_sales': yesterday_sales,
        'last_seven_days_sales': last_seven_days_sales

    }
    return render(request, 'adminsection/dashboard.html', context)


@staff_member_required
def addservice(request):
    """
        Admin can add Service and Price.
    """ 
    form = AddServiceForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('manageservices')
    context = {
        'form': form
    }

    return render(request, 'adminsection/add-services.html', context)


@staff_member_required
def manageservices(request):
    """
        Admin can check the service list.
    """ 
    Services = Service.objects.order_by('-TimeStamp')

    context = {
        'Services': Services
    }
    return render(request, 'adminsection/manage-services.html', context)


@staff_member_required
def updateservice(request, id):
    """
        Admin can update any service.
    """ 
    service = get_object_or_404(Service, id=id)
    form = AddServiceForm(request.POST or None, instance=service)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('manageservices')

    context = {
        'form': form
    }
    return render(request, 'adminsection/edit-services.html', context)


@staff_member_required
def addcustomer(request):
    """
        Admin can add customer details.
    """ 
    form = AddCustomerForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('customerlist')
    context = {

        'form': form,
    }
    return render(request, 'adminsection/add-customer.html', context)


@staff_member_required
def customerlist(request):
    """
        Customer list.
    """ 

    CustomerList = Customer.objects.order_by('-CreateDate')

    context = {
        'CustomerList': CustomerList
    }
    return render(request, 'adminsection/customer-list.html', context)


@staff_member_required
def editcustomer(request, id):
    """
        Edit customer details.
    """ 

    customer = get_object_or_404(Customer, id=id)
    form = AddCustomerForm(request.POST or None, instance=customer)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('customerlist')

    context = {
        'form': form
    }
    return render(request, 'adminsection/edit-customer-detailed.html', context)


@staff_member_required
def assignservices(request, id):
    """
       Can assign services for  Customer.
    """ 

    customer = get_object_or_404(Customer, id=id)
    Services = Service.objects.order_by('-TimeStamp')

    if request.method == 'POST':
        # total_price=request.POST['total_price']
        # discount_price=request.POST['discount_price']
        serviceid = request.POST.getlist('serviceid')

        # if discount_price:
        #     final_price=int(total_price)-int(discount_price)
        #     a1=Invoice(Note=final_price)

        # else:
        #     a1=Invoice()

        instance = Invoice()
        instance.Customer = customer
        instance.save()
        for obj in serviceid:
            instance.Catagories.add(obj)

        return redirect(reverse("viewinvoice", kwargs={
            'id': instance.id
        }))
    context = {
        'Services': Services,
        'customer': customer
    }

    return render(request, 'adminsection/add-customer-services.html', context)


@staff_member_required
def allappointment(request):

    """
        Appointment Lists.
    """ 
    Appoinments = Appoinment.objects.order_by('-ApplyDate')
    context = {
        'Appoinments': Appoinments
    }
    return render(request, 'adminsection/all-appointment.html', context)


@staff_member_required
def viewappointment(request, id):
    """
        View appointment.
    """ 

    Appoinments = get_object_or_404(Appoinment, id=id)
    form = AppoinmentUpdateForm(request.POST or None, instance=Appoinments)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # return redirect('manageservices')
    context = {
        'Appoinment': Appoinments,
        'form': form
    }
    return render(request, 'adminsection/view-appointment.html', context)


@staff_member_required
def newappointment(request):
    """
        New appointments list.
    """ 

    Acceptedappoinments = Appoinment.objects.filter(Remark='')
    context = {
        'Acceptedappoinments': Acceptedappoinments,
    }
    return render(request, 'adminsection/new-appointment.html', context)


@staff_member_required
def acceptedappointment(request):
    """
        Accepted appointments list.
    """ 

    Acceptedappoinments = Appoinment.objects.filter(Remark=1)

    context = {
        'Acceptedappoinments': Acceptedappoinments,
    }
    return render(request, 'adminsection/accepted-appointment.html', context)


@staff_member_required
def rejectedappointment(request):
    """
        Rejected appointments.
    """ 
    Rejectedtedappoinments = Appoinment.objects.filter(Remark=0)

    context = {
        'Rejectedtedappoinments': Rejectedtedappoinments,
    }
    return render(request, 'adminsection/rejected-appointment.html', context)


@staff_member_required
def invoices(request):
    """
        Invoice lists.
    """ 

    invoices = Invoice.objects.order_by('-id')

    context = {
        'invoices': invoices
    }
    return render(request, 'adminsection/invoices.html', context)


@staff_member_required
def viewinvoice(request, id):
    """
        view Invoice .
    """ 

    invoice = get_object_or_404(Invoice, id=id)
    total = Invoice.objects.filter(id=id).aggregate(Sum('Catagories__Cost'))

    context = {
        'invoice': invoice,
        'total': total
    }
    return render(request, 'adminsection/view-invoice.html', context)


@staff_member_required
def searchappointment(request):
    appointment_list = ''
    query = request.GET.get('searchdata')
    if query:
        appointment_list = Appoinment.objects.all()
        appointment_list = appointment_list.filter(
            Q(AppointmentNumber__iexact=query) |
            Q(Name__icontains=query) |
            Q(Email__iexact=query)
        ).distinct()

    context = {

        'appointment_list': appointment_list,
        'query': query
    }

    return render(request, 'adminsection/search-appointment.html', context)


@staff_member_required
def searchinvoices(request):

    query = request.GET.get('searchdata')

    invoice = Invoice.objects.filter(BillingNumber=query)

    context = {
        'invoice': invoice,
        'query': query
    }
    return render(request, 'adminsection/search-invoices.html', context)


@staff_member_required
def bwdatesreportsds(request):

    invoice_list = ''
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    if from_date and to_date:

        invoice_list = Invoice.objects.all()

        invoice_list = invoice_list.filter(
            Q(Date__gte=from_date),
            Q(Date__lte=to_date)
        ).distinct()
    context = {

        'invoice_list': invoice_list,
        'from_date': from_date,
        'to_date': to_date
    }

    return render(request, 'adminsection/bwdates-reports-ds.html', context)


@staff_member_required
def profile(request):
    return render(request, 'adminsection/admin-profile.html')


@staff_member_required
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'adminsection/change-password.html', {
        'form': form
    })


def forgetpassword(request):
    return render(request, 'adminsection/forget-password.html')


def contactus(request):
    return render(request, 'adminsection/contact-us.html')


@staff_member_required
def adminprofile(request):
    return render(request, 'adminsection/admin-profile.html')


def logout(request):
    auth.logout(request)
    return redirect('signin')
