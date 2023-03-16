"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from polls.views import hello,hello1,hello2,hello3,students
from students.views import listone, listall,post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hello),
    path('hello1/<str:username>',hello1),
    path('hello2/<str:username>',hello2),
    path('hello3/<str:username>',hello3),
    path('stds',students),
    path('listone/', listone),
    path('listall/', listall),
    path('post/', post),
    ]
