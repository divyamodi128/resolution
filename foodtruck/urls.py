from django.conf.urls import url
from .views import (
    getLists, create, update, 
    ListTruckView,
    CreateTruckView,
    DetailTruckView,
    FormTruckView,
    UpdateTruckView,
    DeleteTruckView,
)

urlpatterns = [
    url(r'^trucklist/', getLists),
    # url(r'^?P<pk>[^0-9]+$', update),
    url(r'^create/', CreateTruckView.as_view(), name='truck-create'),
    url(r'^form/', FormTruckView.as_view()),
    url(r'^list/', ListTruckView.as_view(), name='truck-list'),
    url(r'^details/(?P<pk>[0-9]+)/$', DetailTruckView.as_view(), name='truck-details'),
    url(r'^edit/(?P<pk>[0-9]+)/$', UpdateTruckView.as_view(), name='truck-updates'),
    url(r'^delete/(?P<pk>[0-9]+)/$', DeleteTruckView.as_view(), name='truck-delete'),
]