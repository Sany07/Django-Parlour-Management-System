from django import forms
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