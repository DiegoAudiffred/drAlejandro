from pyexpat.errors import messages
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from db.models import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib.auth.decorators import user_passes_test,login_required

from Index.forms import *

def index(request):
    doctors = Doctor.objects.all()
    services = Service.objects.all()
    context = {
        'doctors': doctors,
        'services':services,
        
    }
    print(doctors)
    return render(request, 'Index/index.html',context)

def peopleBanner(request):
 
    return render(request, 'Index/peopleBanner.html')

def contactPage(request):
    formContacto = ContactoForm()
    return render(request, 'Index/contactPage.html', {'formContacto': formContacto})

def serviciosPage(request):
    servicios = Service.objects.all()
    return render(request, 'Index/serviciosPage.html', {'servicios': servicios})


def uploadInfo(request):
    if request.method == 'POST':
        formContacto = ContactoForm(request.POST, request.FILES)
        if formContacto.is_valid():
            formContacto.save()
            return redirect('Index:contactPage')
    else:
        formContacto = ContactoForm()

    return render(request, 'Index/contactPage.html', {'formContacto': formContacto})


def sendMail():
    pass

def iniciarsesion():
    pass