from django.conf.urls import url
from .views import (
    getLists, create, update, 
    TruckListView,
    CreateTruckView,
)

urlpatterns = [
    url(r'^trucklist/', getLists),
    # url(r'^?P<pk>[^0-9]+$', update),
    url(r'^create/', CreateTruckView.as_view(), name='truck-create'),
    url(r'^list/', TruckListView.as_view(), name='truck-list'),
]