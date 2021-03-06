"""numeronBackend URL Configuration

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
from django.urls import include,path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,  name="index"),
    path('getRooms/',views.getRooms,name="getRooms"),
    path('getRoom/',views.getRoom,name="getRoom"),
    path('getGuess/',views.getGuess,name="getGuess"),
    path('createRoom/', views.createRoom,  name="createRoom"),
    path('joinRoom/', views.joinRoom,  name="joinRoom"),
    path('leftRoom/', views.leftRoom,  name="leftRoom"),
    path('setCode/', views.setCode,  name="setCode"),
    path('setStart/', views.setStart,  name="setStart"),
    path('createGuess/', views.createGuess,  name="createGuess"),
    path('checkCode/', views.checkCode,  name="checkCode"),
    path('getCount/', views.getCount,  name="getCount"),

    path('deleteHistory/', views.deleteHistory,  name="deleteHistory"),
]
