from django.contrib import admin

# Register your models here.
from . models import *

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['cat_name','slug','image']
    list_editable = ['image']
    prepopulated_fields = {'slug':('cat_name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):

    list_display = ['p_name','price','p_slug','stock','avail','created','updated','image']
    list_editable = ['price','stock','avail','image']
    prepopulated_fields = {'p_slug':('p_name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)