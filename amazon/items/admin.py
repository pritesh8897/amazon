from django.contrib import admin
from .models import myusers,Accessories,Mobile,products
from django.contrib.auth.admin import UserAdmin

class UserAdmin(UserAdmin,admin.ModelAdmin):
    list_display_links = ('first_name','username')

# Register your models here.
admin.site.register(myusers,UserAdmin)
admin.site.register(Accessories)
admin.site.register(Mobile)
admin.site.register(products)


UserAdmin.fieldsets += ("custom fields set",{'fields':('company','phone_number','message','city','gender')}),

