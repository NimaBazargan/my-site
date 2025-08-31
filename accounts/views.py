from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import UserEditForm, CustomUserCreationForm,CustomAuthenticationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.db.models import Q


def login_view(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = CustomAuthenticationForm(request.POST)
            if form.is_valid():
                username_email = form.cleaned_data.get("username_email")
                password = form.cleaned_data.get("password")
                user = User.objects.get(Q(username=username_email) | Q(email=username_email))
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.add_message(request,messages.SUCCESS,'success')
                    return redirect('/')
                else:
                    messages.add_message(request,messages.ERROR,'The user dose not exist or Password is incorrect')
            else:
                for errors in form.errors.values():
                    for error in errors:
                        messages.add_message(request,messages.ERROR,f'{error}')
        else:
            form = CustomAuthenticationForm()
        context = {'form' : form}
        return render(request,'accounts/login.html', context)
    else:
        return redirect('/')
    
@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'success')
                return redirect('login')
            else:
                for errors in form.errors.values():
                    for error in errors:
                        messages.add_message(request,messages.ERROR,f'{error}')
        else:
            form = CustomUserCreationForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')
    
@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST,instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
                user.save()
                update_session_auth_hash(request, user)
            else:
                user.save()
            messages.add_message(request,messages.SUCCESS,'success')
            return redirect('login')
        else:
            for errors in form.errors.values():
                for error in errors:
                    messages.add_message(request,messages.ERROR,f'{error}')
    else:
        form = UserEditForm(instance=user)
    context = {'form' : form}
    return render(request,'accounts/profile.html', context)   
