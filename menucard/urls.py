from django.conf.urls import url
from .views import MenuCreate

urlpatterns = [
    url(r'^create/', MenuCreate.as_view(), name='truck-create'),
    # url(r'^list/', ListTruckView.as_view(), name='truck-list'),
    # url(r'^details/(?P<pk>[0-9]+)/$', DetailTruckView.as_view(), name='truck-details'),
    # url(r'^edit/(?P<pk>[0-9]+)/$', UpdateTruckView.as_view(), name='truck-updates'),
    # url(r'^delete/(?P<pk>[0-9]+)/$', DeleteTruckView.as_view(), name='truck-delete'),
]