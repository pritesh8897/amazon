from django.contrib import admin
from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('products',views.productlist.as_view(),name = 'product_page'),#classbased product page
    path('',views.home,name = 'home'),
    path('/products',views.productlist,name = 'product_page'),#function based product page
    path('productdetails/<int:i_id>/',views.productdetails,name = 'detail_page'),
    path('productdetails2/<int:j_id>/', views.productdetails2, name='detail_page2'),
    path('Mcreate',views.Mcreateview.as_view(),name = 'M_create'),
    path('Acreate',views.Acreateview.as_view(),name = 'A_create'),
    path('Aedit/<int:j_id>/',views.Aeditview.as_view(),name = 'A_edit'),
    path('Medit/<int:pk>/', views.Meditview.as_view(), name='M_edit'),
    path('Adelete/<int:j_id>/',views.Adeleteview.as_view(),name='A_delete'),
    path('Mdelete/<int:pk>/',views.Mdeleteview.as_view(),name='M_delete'),
    path('Mfilter',views.MFilterview.as_view(),name='M_filter'),
    path('contact', views.contactview.as_view(), name='contact_page'),


]
