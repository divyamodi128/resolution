from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'gender', 'attribute', 'location', 'birth_date', 'email_confirmed')
    list_display_links = ('user',)

admin.site.register(Profile, ProfileAdmin)
