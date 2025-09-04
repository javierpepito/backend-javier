from django.http import HttpResponse
from django.shortcuts import render
from.models import Producto

def inicio(request):
    nombre = "Javier Mendez"
    return HttpResponse(F"¡Bienvenidos a mi primera app Django, {nombre}!")

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos}) 