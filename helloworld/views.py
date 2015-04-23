from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def helloworld(request):
    return render(request, 'hello_world/hello_world.html')