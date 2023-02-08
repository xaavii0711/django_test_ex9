from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, Rul</h1> <p>You're at the <b>polls</b> index.</p>")


def test(request):
    return HttpResponse("Test View")