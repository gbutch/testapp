from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext


def helloworld(request, name):
    return render(request, 'hello_world/hello_world.html', {'name':name})