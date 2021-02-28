"""Project URL Configuration

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('contact', views.contact, name = 'contact'),
    path('about', views.about, name = 'about'),
    path('result', views.result, name = 'result'),
    path('result_beginner', views.result_beginner, name = 'result_beginner'),
    path('result_intermidiate', views.result_intermidiate, name = 'result_intermidiate'),
    path('result_advance', views.result_advance, name = 'result_advance'),
]
