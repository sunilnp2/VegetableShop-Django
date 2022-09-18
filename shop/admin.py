from django.contrib import admin
from shop.models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug']
    list_display_links =['id','name', 'slug']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'dis_price']

    list_display_links = ['id', 'name', 'price', 'dis_price']

class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'description']
    list_display_links = ['id', 'heading', 'description']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Slider, SliderAdmin)
