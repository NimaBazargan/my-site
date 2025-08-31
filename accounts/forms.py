from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q

class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2',]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use. Please supply a different email address.")
        return email

class CustomAuthenticationForm(forms.ModelForm):
    username_email = forms.CharField(label='Username or Email', max_length=255)

    class Meta:
        model = User
        fields = ['username_email','password',]

    def clean_username_email(self):
        username_email = self.cleaned_data.get('username_email')
        users = User.objects.filter(Q(username=username_email) | Q(email=username_email))
        if not users.exists():
            raise forms.ValidationError("The user doesn't exist or Password is incorrect.")
        return username_email
    
    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     users = User.objects.filter(password=password)
    #     if not users.exists():
    #         raise forms.ValidationError("password is incorrect")
    #     return password