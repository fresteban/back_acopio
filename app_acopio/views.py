from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wena(request):
    return HttpResponse("<h1>Wena wena wena, wena</h1>")
