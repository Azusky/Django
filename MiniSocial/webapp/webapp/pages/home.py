from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('page--home.html')

    return HttpResponse(template.render({'subtitle': 'Hey, all good!'}, request))
