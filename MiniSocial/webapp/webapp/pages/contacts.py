from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template(
            'pages/templates/page--contacts.html'
            )

    return HttpResponse(template.render({'subtitle': 'contacts!'}, request))
