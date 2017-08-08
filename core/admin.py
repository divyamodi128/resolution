from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email_confirmed',)
    list_display_links = ('id',)

admin.site.register(Profile, ProfileAdmin)
