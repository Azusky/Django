from django.http import HttpResponse
from django.template import loader
from webapp.users.user import User


usersList = [
    User("Johny", "j@example.com", "1.png", "qwerty1"),
    User("Mary", "m@example.com", "2.png", "qwerty2"),
    User("Petter", "p@example.com", "3.png", "qwerty3")
]

def showProfileList(request):
    template = loader.get_template(
            'users/templates/profile--list.html'
            )
    return HttpResponse(template.render({'profiles': usersList,}, request))

def createProfile(request):
    template = loader.get_template(
            'users/templates/profile--create.html'
            )
    return HttpResponse(template.render({'profiles': usersList,}, request))


def saveProfile(request):
    username = request.GET['username']
    email = request.GET['email']
    password = request.GET['password']

    usersList.append(User(username, email,'', password))
    return HttpResponse("Your account has been saved")

def showProfile(request):
    return HttpResponse('This is the user profile')

def editProfile(request):
    return HttpResponse('editing profile')

def deleteProfile(request):
    return HttpResponse('deleting profile')
