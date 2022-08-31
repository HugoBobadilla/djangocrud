from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(forms.ModelForm):  
  class Meta:  
    model = Contact
    fields = "__all__"  
  
  # first_name = forms.CharField(label='First Name')
  # last_name = forms.CharField(label='Last Name')
  # phone_number = forms.CharField(label='Phone Number')
  # address = forms.CharField(label="Address")
  # fields = ["first_name", "last_name", "phone_number", "address"]