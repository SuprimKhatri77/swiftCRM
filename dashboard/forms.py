from django import forms 
from .models import CustomerDetail


class AddNewRecordForm(forms.ModelForm):
    class Meta:
        model = CustomerDetail
        fields = ['first_name','last_name','email','phone_number','address','city','province','country']


class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = CustomerDetail
        fields = ['first_name','last_name','email','phone_number','address','city','province','country']