from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<name>[a-zA-z]+)?$', views.helloworld)
]
