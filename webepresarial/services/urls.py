from django.urls import path
from . import views

urlpatterns = [
    #path del nucleo
    path('',views.services, name="services"),
]



