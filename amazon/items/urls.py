from django.contrib import admin
from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('products',views.productlist.as_view(),name = 'product_page'),#classbased product page
    path('',views.Productlist.as_view(),name='product_list'),
    path('productDetail/<int:product_id>/',views.Productdetail.as_view(),name='product_detail'),
    path('category/product/<int:pk>',views.Filter.as_view(),
         name='product_filter_category'),
    path('brand/product/<int:pk>',views.Filter.as_view(),
         name='product_filter_brand'),
    path('search',views.Searchview.as_view(),name='search_view'),

    path('contact', views.contactview.as_view(), name='contact_page'),


]
