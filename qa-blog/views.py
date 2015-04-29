from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext


def simulated_annealing(request):
    return render(request, 'qa-blog/simulated-annealing.html')