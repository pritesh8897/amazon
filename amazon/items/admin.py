from django.contrib import admin
from .models import myusers,ProductDetail,Product,Category,Color,Brand
from django.contrib.auth.admin import UserAdmin

class UserAdmin(UserAdmin,admin.ModelAdmin):
    list_display_links = ('first_name','username')

# Register your models here.
admin.site.register(myusers,UserAdmin)
admin.site.register(ProductDetail)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Brand)



UserAdmin.fieldsets += ("custom fields set",{'fields':('company','phone_number','message','city','gender')}),

