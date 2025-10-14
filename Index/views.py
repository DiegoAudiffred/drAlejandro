from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from db.models import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib.auth.decorators import user_passes_test,login_required

from Index.forms import *

def index(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors,
        
    }
    print(doctors)
    return render(request, 'Index/index.html',context)

def peopleBanner(request):
 
    return render(request, 'Index/peopleBanner.html')

def contactPage(request):
    formContacto= ContactoForm()
    return render(request, 'Index/contactPage.html',context={'formContacto':formContacto})

def uploadInfo():
    pass

def sendMail():
    pass