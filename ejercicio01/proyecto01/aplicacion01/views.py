from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.
def home(request):
    saludo = "Hola mundo"    
    return render_to_response("home.html", {"saludo":saludo})









