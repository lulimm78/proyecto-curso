from django.shortcuts import render
from .models import Rectificado

# Create your views here.
def rectificados(request):
    rectificados = Rectificado.objects.all()
    return render(request, "rectificados/rectificados.html", {'rectificados':rectificados})
