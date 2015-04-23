from django.http import HttpResponse
from django.template import loader

def helloworld(request):
    template = loader.get_template('helloworld/helloworld.html')
    return HttpResponse(template.render())