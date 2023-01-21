from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html",)

# def add(request):
#     x = int(request.GET['n1'])
#     y = int(request.GET['n2'])
#     r = x + y
#     return render(request, "register.html", {'res': r})
