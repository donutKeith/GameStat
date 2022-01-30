from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return HttpResponse("Hello World")


def say_hello_render(request):
    return render(request, "hello.html", {"name": "Keith"})
