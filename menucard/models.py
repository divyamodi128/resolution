from django.db import models
from django.conf import settings
from foodtruck.models import Truck
from resolutions.helpers import RandomFileName

# Create your models here.
class Menu(models.Model):
    name =          models.CharField(max_length=250, blank=False, null=False, help_text="Menu Card Name")
    truck =         models.ForeignKey(Truck, on_delete=models.CASCADE)
    user =          models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image =         models.ImageField(upload_to=RandomFileName('Menu-Images'), blank=True, null=True, 
                                      default='/media/Menu-Images/default.jpg')
    description =   models.TextField()
    is_dish =       models.BooleanField(default=False)
    
    def __str__(self):
        return self.name