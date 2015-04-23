from django.http import HttpResponse
from django.template import loader

def helloworld(request):
    template = loader.get_template('hello_world/hello_world.html')
    return HttpResponse(template.render())