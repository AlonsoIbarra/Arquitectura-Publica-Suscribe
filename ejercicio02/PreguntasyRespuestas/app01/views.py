from django.shortcuts import render
from django.http import HttpResponse
from app01.models import Pregunta, Respuesta

# Create your views here.
def index(request):
    preguntas = Pregunta.objects.all()
    respuesta_string = "Preguntas <br/>"
    respuesta_string += '<br/>'.join(["id: %s, asunto: %s"%(p.id, p.asunto) for p in preguntas])
    return HttpResponse(respuesta_string)
