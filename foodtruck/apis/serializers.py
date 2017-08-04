from rest_framework import serializers
from ..models import Truck

class FoodTruckSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Truck
        fields = ('url', 'name', 'website', 'user', 'contact_no', 'emails', 'description')