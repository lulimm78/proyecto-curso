from django.urls import path
from . import views

urlpatterns = [
    #path del nucleo
    path('',views.rectificados, name="rectificados"),
]



