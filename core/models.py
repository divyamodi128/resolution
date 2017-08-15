from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    NONE = 'NONE'
    USER = 'USER'
    DRIVER = 'DRIVER'
    MODE_OF_USER = (
        (NONE, 'none'),
        (USER, 'user'),
        (DRIVER, 'truck_driver'),
    )
    GENDER = (
        ('M', 'M'),
        ('F', 'F'),
        ('U', 'N'),
    )
    user =        models.OneToOneField(User, on_delete=models.CASCADE)
    image =       models.ImageField(upload_to='User-Profiles', blank=True, null=True, default='/media/User-Profiles/default.png')
    attribute =   models.CharField(max_length=13, choices=MODE_OF_USER, default=NONE)
    gender =      models.CharField(max_length=1, choices=GENDER, default='U')
    birth_date =  models.DateField(null=True, blank=True)
    bio =         models.TextField(null=True, blank=True, default='No Bios', help_text='Short Descriptions about yourself')
    location =    models.CharField(max_length=30, blank=True)
    email_confirmed =   models.BooleanField(default=False)
    # other fields...

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
