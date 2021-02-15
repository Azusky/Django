from django.http import HttpResponse

def homePage(request):
    return HttpResponse('Hello')
