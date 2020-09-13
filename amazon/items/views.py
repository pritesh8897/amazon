from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView,FormView)
from items.forms import SignupForm,ContactForm
from items.models import myusers,ProductDetail,Category,Brand

from django.db.models import Q  #for logical operation like OR AND NOR NAND



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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brand'] = Brand.objects.all()
        print(context)
        return context



class Productdetail(DetailView):
    model = ProductDetail
    template_name = 'items/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brand'] = Brand.objects.all()
        print(context)
        return context

# here productlist view inherit in this class bcz we needed get_context_data of productList
# due to navbar's dropdown links.otherwise put get_context_data here in this class
class Filter(Productlist,ListView):
    model = ProductDetail
    template_name = 'items/product_list.html'
    context_object_name = 'product_list'

    def get_queryset(self,*args,**kwargs):
        query_set = super(Filter,self).get_queryset(*args,**kwargs)

        pk = self.request.resolver_match.kwargs.get('pk')
        url = self.request.resolver_match.url_name

        if pk:
            if url == 'product_filter_category':
                query_set = query_set.filter(product__category__id=pk)
                # query_set = ProductDetail.objects.filter(product__category__id=pk)  (u can use)
            elif url == 'product_filter_brand':
                query_set = query_set.filter(product__brand__id=pk)
            else:
                return query_set
        else:
            return query_set

        return query_set


# here productlist view inherit in this class bcz we needed get_context_data of productList
# due to navbar's dropdown links.otherwise put get_context_data here in this class
class Searchview(Productlist,ListView):
    model = ProductDetail
    template_name = 'items/product_list.html'
    context_object_name = 'search_result'

    def get_queryset(self,*args,**kwargs):
        queryset = super(Searchview,self).get_queryset(*args,**kwargs)

        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(Q(product__brand__name__icontains = q)|Q(product__name__icontains = q)|
                                       Q(product__category__name__icontains = q)|
                                       Q(product__price__icontains = q)|Q(colors__name__icontains = q))
        print(queryset)
        return queryset

















