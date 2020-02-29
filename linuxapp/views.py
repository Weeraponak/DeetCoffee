from django.shortcuts import render,redirect
from django.utils import encoding #smart_unicode
from urllib.parse import parse_qsl
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Service

# Create your views here.
def services(req):
    if req.method == 'POST':
        post = req.POST
        s = Service()
        s.icon = post['icon']
        s.title = post['title']
        s.detail = post['detail']
        s.save()
        services = Service.objects.all()
        print(services)
        return render(req, 'linuxapp/services.html', { 'services': services })
    else:
        print('ร้องขอทำมะดา')
        services = Service.objects.all()
        print(services)
        return render(req, 'linuxapp/services.html', { 'services': services })


def index(req):
    return render(req, 'linuxapp/index.html')

def about(req):
    return render(req, 'linuxapp/about.html')

def products(req):
    return render(req, 'linuxapp/products.html')

def store(req):
    return render(req, 'linuxapp/store.html')


def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
    
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(req, user)
            return redirect('/')
        else:
            messages.info(req,'invalid credentials')
            return render(req,'linuxapp/login.html')

    else:
        return render(req,'linuxapp/login.html')


def register(req):
    if req.method == 'POST':
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        username = req.POST['username']
        password1 = req.POST['password1']
        password2 = req.POST['password2']
        email = req.POST['email']


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(req,'Username Taken')
                return render(req,'linuxapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(req,'Email Taken')
                return render(req,'linuxapp/register.html')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return render(req,'linuxapp/login.html')

        
        else:
            messages.info(req,'password not matching..')
            return render(req,'linuxapp/register.html')
        return redirect('/')

        
        
    else:
        return render(req, 'linuxapp/register.html')


def logout(req):
    auth.logout(req)
    return redirect('/')
