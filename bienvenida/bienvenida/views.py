from django.http import HttpResponse
def inicio(request):
    nombre = "Javier Mendez"
    return HttpResponse(F"¡Bienvenidos a mi primera app Django, {nombre}!")
    