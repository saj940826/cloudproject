
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('login/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def game(request, num=1):
    template = loader.get_template('login/game.html')
    context = {}
    return HttpResponse(template.render(context, request))

# Create your views here.
