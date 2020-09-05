from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from items.models import myusers



class SignupForm(UserCreationForm):
    class Meta:
        model = myusers
        # fields = '__all__'
        fields = ['username','first_name','last_name','email','password1','password2','company','phone_number','city','gender']


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone = forms.CharField(max_length=10,help_text='enter your 10 digit phone number')
    message = forms.CharField(widget=forms.Textarea,required=False)

