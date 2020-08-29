from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView,FormView)
from django.contrib.auth.models import User
from items.forms import SignupForm,ContactForm,mobileform,Accessoriesform
from items.models import myusers,products,Mobile,Accessories



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


# class productlist(ListView):
#     model = products
#     template_name = 'items/products.html'
#     context_object_name = 'i'

def home(request):
    M1 = Mobile.objects.all()
    A1 = Accessories.objects.all()
    context = {}
    context['Mobile_object'] = M1
    context['Accessories_object'] = A1
    return render(request, 'items/home.html', context,)

def productlist(request):
    M1 = Mobile.objects.all()
    A1 = Accessories.objects.all()
    context = {}
    context['Mobile_object'] = M1
    context['Accessories_object'] = A1
    return render(request, 'items/products.html',context )

def productdetails(request,i_id):
    product_object = Mobile.objects.get(id=i_id)
    return render(request,'items/productsdetail.html',{'product':product_object})

def productdetails2(request,j_id):
    product_object2 = Accessories.objects.get(id=j_id)
    return render(request,'items/productdetail2.html',{'product2':product_object2})

class Mcreateview(CreateView):
    model = Mobile
    form_class = mobileform
    template_name = 'items/Mobile_create.html'
    success_url = '/home/products'

class Acreateview(CreateView):
    model = Accessories
    form_class = Accessoriesform
    template_name = 'items/Accessories_create.html'
    success_url = '/home/products'

class Aeditview(UpdateView):
    model = Accessories
    form_class = Accessoriesform
    template_name = 'items/Accessories_edit.html'
    success_url = '/home/products'
    pk_url_kwarg = 'j_id'

class Meditview(UpdateView):
    model = Mobile
    form_class = mobileform
    template_name = 'items/Mobile_edit.html'
    success_url = '/home/products'

class Adeleteview(DeleteView):
    model = Accessories
    template_name = 'items/Accessories_delete.html'
    success_url = '/home/products'
    pk_url_kwarg = 'j_id'

class Mdeleteview(DeleteView):
    model = Mobile
    template_name = 'items/Mobile_delete.html'
    success_url = '/home/products'


class MFilterview(ListView):
    model = Mobile
    template_name = 'items/Mobile_Filter.html'
    context_object_name = 'filter'

    def get_queryset(self,*args,**kwargs):
        queryset = super(MFilterview, self).get_queryset(*args, **kwargs)
        print(queryset)

        q = self.request.user.id
        print(q)
        p = Mobile.objects.get(id)
        print(p)














    # def get_context_data(self,**kwargs):
    #     context={}
    #     context = super().get_context_data(**kwargs)
    #     context[filter] = Mobile.objects.get(id)
    #     return context
