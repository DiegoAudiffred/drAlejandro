from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from db.models import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib.auth.decorators import user_passes_test,login_required

def index(request):
    blogs = Blog.objects.all().order_by('-publicationDate')
    blog_groups = [blogs[i:i+3] for i in range(0, len(blogs), 3)]
    return render(request, 'Index/index.html', {'blog_groups': blog_groups,'blogs':blogs})
