from django.http import HttpResponse


def showFriendsList(request):
    return HttpResponse('Friends List')

def addFriend(request):
    return HttpResponse('Add Friend')


def removeFriend(request):
    return HttpResponse('Remove Friend')
