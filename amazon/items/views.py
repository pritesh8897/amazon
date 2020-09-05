from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView,FormView)
from items.forms import SignupForm,ContactForm
from items.models import myusers,ProductDetail



# Create your views here.


class signupview(CreateView):
    model = myusers
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = '/'

class contactview(FormView):
    template_name = 'items/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)

        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone')
        message = form.cleaned_data.get('message')

        # print(email)

        myuser_obj = myusers(
             username = email,
             first_name=first_name,
             last_name=last_name,
             email=email,
             phone_number = phone,
             message = message)

        myuser_obj.save()
        return super().form_valid(form)

def LogoutView(request):
    logout = (request)
    return redirect ('/')


class Productlist(ListView):
    model = ProductDetail
    template_name = 'items/product_list.html'
    context_object_name = 'product_list'

class Productdetail(DetailView):
    model = ProductDetail
    template_name = 'items/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'


















