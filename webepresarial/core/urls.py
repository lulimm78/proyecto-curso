from django.urls import path
from . import views

urlpatterns = [
    #path del nucleo
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('store/',views.store, name="store"),
]