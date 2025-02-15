from django.shortcuts import render,redirect
from .models import *
from .forms import AddNewRecordForm,UpdateRecordForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')
    return render(request,'dashboard/index.html')

@login_required
def dashboard(request):
    details = CustomerDetail.objects.filter(user=request.user)
    context = {
        'details':details
    }
    return render(request,'dashboard/dashboard.html',context)

@login_required
def add_new_record_view(request):
    if request.method == 'POST':
        form = AddNewRecordForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('dashboard:dashboard')
    else:
        form = AddNewRecordForm()
    return render(request,'dashboard/add_new_record.html',{'form':form})

@login_required
def view_record(request,pk):
    record = CustomerDetail.objects.get(user=request.user,pk=pk)
    context = {
        'record':record
    }
    return render(request,'dashboard/view_record.html',context)


@login_required
def update_record_view(request,pk):
    record = CustomerDetail.objects.get(user=request.user, pk=pk)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard')
    else:
        form = UpdateRecordForm(instance=record)
    return render(request,'dashboard/update_record.html',{'form':form})
