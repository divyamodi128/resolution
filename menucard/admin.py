from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'truck', 'user',)
    list_display_links = ('name',)

admin.site.register(Menu, MenuAdmin)