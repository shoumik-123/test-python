from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def blog1(request):
    return HttpResponse('<h1>blog 1 </h1>')
