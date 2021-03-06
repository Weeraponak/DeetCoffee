"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from linuxapp import views as linuxappviews
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', linuxappviews.index),
    path('services', linuxappviews.services),
    path('admin/', admin.site.urls),
    path('index', linuxappviews.index),
    path('about', linuxappviews.about),
    path('products', linuxappviews.products),
    path('store', linuxappviews.store),
    path('register', linuxappviews.register),
    path('login', linuxappviews.login),
    path('logout', linuxappviews.logout),
]

