from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from db.models import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib.auth.decorators import user_passes_test,login_required

def index(request):
    return render(request, 'Index/index.html')