from django.db import models
from django.conf import settings

# Create your models here.
class Truck(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False, help_text="Give your Truck a Nice Name")
    website = models.CharField(max_length=250, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    emails = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name