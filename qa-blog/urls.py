from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^simulated-annealing', views.simulated_annealing)
]
