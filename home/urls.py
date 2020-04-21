from django.conf.urls import url
from .views import locations, contact, index

urlpatterns = [
    url(r'^locations/', locations, name='locations'),
    url(r'^contact/', contact, name='contact'),
    url(r'^&', index, name='index'),
]