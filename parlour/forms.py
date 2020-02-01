from django import forms
from parlour.models import *


class AppoinmentForm(forms.ModelForm):

    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    Email = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    PhoneNumber = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

    AppoinmentDate = forms.CharField( widget=forms.TextInput(attrs={

        'placeholder': 'Date',
        'class':'appointment_date'

    }))

    AppoinmentTine = forms.CharField( widget=forms.TextInput(attrs={
        
        'placeholder': 'Time ',
        'class':'appointment_time'
    }))
    


    class Meta:

        model=Appoinment
        fields =[
            'Name',
            'Email',
            'PhoneNumber',
            'Service',
            'AppoinmentDate',
            'AppoinmentTine',

        ]

  
    def clean_service(self):
        Service = self.cleaned_data.get('Service')
  
        if not Service:
            raise forms.ValidationError("Service is required")
        return Service
    