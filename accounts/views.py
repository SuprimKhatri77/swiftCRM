from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,'Registration successful!')
            return redirect('dashboard:dashboard')
        else:
            messages.error(request,'Please correct the errors below')

    else:
        form = RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username =  form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                messages.success(request,'Logged in successfully!')
                return redirect('dashboard:dashboard')
        else:
            messages.error(request,'Inavlid username or password')
    else:
        form = LoginForm()

    return render(request,'accounts/login.html',{'form':form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request,'Logged out successfully!')
    return redirect('dashboard:index')

