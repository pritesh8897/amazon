from django.contrib import admin
from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('products',views.productlist.as_view(),name = 'product_page'),#classbased product page
    path('',views.Productlist.as_view(),name='product_list'),
    path('productDetail/<int:product_id>/',views.Productdetail.as_view(),name='product_detail'),
    path('contact', views.contactview.as_view(), name='contact_page'),


]
