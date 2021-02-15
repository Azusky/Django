from django.http import HttpResponse
from django.template import loader


def showProfileList(request):
    template = loader.get_template(
            'users/templates/profile--list.html'
            )
    return HttpResponse(template.render({'profiles': ['Jon', 'Mary', 'Peter'],}, request))


def showProfile(request):
    return HttpResponse('This is the user profile')

def editProfile(request):
    return HttpResponse('editing profile')

def deleteProfile(request):
    return HttpResponse('deleting profile')
