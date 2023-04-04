from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def diga_oi(request):
    return render(request, ‘oi.html’)