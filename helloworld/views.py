from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext


def helloworld(request, name):
    context = {'name':name}
    return render(request, 'hello_world/name.html', context)