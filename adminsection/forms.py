from django import forms
from parlour.models import *
from adminsection.models import *
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class':'user'   
    }))
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={
        
        'placeholder':'Password',
        'class':'lock'
    }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            self.user = authenticate(username=username, password=password)

            if self.user is None:
                raise forms.ValidationError("User Does Not Exist.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not self.user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(LoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user



class AddServiceForm(forms.ModelForm):
    ServiceName = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Service Name',
        'label': "Service Name"
    }))
    Cost = forms.CharField(strip=False,widget=forms.TextInput(attrs={
        
        'placeholder': 'Cost',
        'label': "Cost"
    }))
    class Meta:

        model=Service

        fields =[
            'ServiceName',
            'Cost',
        ]


class AddCustomerForm(forms.ModelForm):

    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    Email = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    PhoneNumber = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    Note = forms.CharField( widget=forms.Textarea(attrs={'placeholder': 'Note'}))



    class Meta:

        model=Customer
        fields =[
            'Name',
            'Email',
            'PhoneNumber',
            'Gender',
            'Note'
        ]          

    def clean_gender(self):
        Gender = self.cleaned_data.get('Gender')
        if not Gender:
            raise forms.ValidationError("Gender required")
        return Gender        
    
    def clean_details(self):
        Note = self.cleaned_data.get('Note')
        if not Note:
            raise forms.ValidationError("Note required")
        return Note    

class AppoinmentUpdateForm(forms.ModelForm):

    Note = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Note If needed'}))

    class Meta:

        model=Appoinment
        fields =[
            'Note',
            'Remark',

        ]

  
    def clean_remark(self):
        Remark = self.cleaned_data.get('Remark')
  
        if not Remark:
            raise forms.ValidationError("Remark is required")
        return Remark
    