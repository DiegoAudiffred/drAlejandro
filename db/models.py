from django.db import models

# Create your models here.
from datetime import timezone
import decimal
import math
import urllib
import json
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q
from django.forms import ImageField
from django.utils import timezone



from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class User(AbstractUser):

    username = None
    email = models.EmailField('Correo electrónico', unique=True, blank=True, null=True)
    first_name = models.CharField("Nombre", max_length=200, null=True, blank=True,unique=True,default="Empleado")
    phone_number = models.CharField("Teléfono", max_length=15, unique=True, null=True)
    url = models.ImageField(upload_to="uploads/gallery/",null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()
    is_active= models.BooleanField(default=True)


    def __str__(self):
        return self.first_name



class Blog(models.Model):
    user = models.ForeignKey(
        User, on_delete = models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    publicationDate = models.DateTimeField(auto_now=True)
    body = models.TextField()
    url = models.ImageField(upload_to="uploads/gallery/")
