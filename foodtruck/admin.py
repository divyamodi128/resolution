from django.contrib import admin
from .models import Truck

# Register your models here.
class TruckAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'emails']
    list_display_links = ['name']

admin.site.register(Truck, TruckAdmin)
