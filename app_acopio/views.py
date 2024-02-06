from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Center, Address, Donation, Donor

# Create your views here.
def wena(request):
    return HttpResponse("<h1>Wena wena wena, wena</h1>")

def acopios(request):
    acopios = list(Center.objects.values())
    return JsonResponse(acopios, safe=False)
