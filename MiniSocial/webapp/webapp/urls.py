"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.users import profile
from webapp.users import friends
from webapp.pages import home
from webapp.pages import contacts

urlpatterns = [
    path('', home.index),
    path('contacts', contacts.index),
    path('users/profiles', profile.showProfileList),
    path('users/profiles/create', profile.createProfile),
    path('users/profiles/save', profile.saveProfile),
    # path('user/profile/edit', profile.editProfile),
    # path('user/profile/delete', profile.deleteProfile),
    # path('user/friends', friends.showFriendsList),
    # path('user/friends/add', friends.addFriend),
    # path('user/friends/remove', friends.removeFriend)
]
