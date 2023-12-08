from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Pregunta


def index(request): 
    preguntas = Pregunta.objects.get(id=1) #Consulta en la BD todos los objetos de la clase Pregunta. ç
    return HttpResponse(f"{preguntas.pregunta}")

#def index(request): 
#    return HttpResponse("Hola mundo desde encuesta!")

#def preguntas(request):
#    preguntas = Pregunta.objects.all() #Consulta en la BD todos los objetos de la clase Pregunta. ç
#    return HttpResponse("Hola mundo desde encuesta!")
