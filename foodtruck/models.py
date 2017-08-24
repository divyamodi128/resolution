from django.db import models
from django.conf import settings

from resolutions.helpers import RandomFileName

# Create your models here.
class Truck(models.Model):
    name =          models.CharField(max_length=250, blank=False, null=False, help_text="Name Your Truck")
    website =       models.CharField(max_length=250, blank=True, null=True)
    image =         models.ImageField(upload_to=RandomFileName('Truck-Images'), blank=True, null=True, 
                                      default='/media/Truck-Images/Default.jpg')
    user =          models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_no =    models.CharField(max_length=15, blank=True, null=True)
    emails =        models.CharField(max_length=100, blank=True, null=True)
    description =   models.TextField()

    def __str__(self):
        return self.name