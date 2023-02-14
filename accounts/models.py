from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from rest_framework.authtoken.models import Token




class User(AbstractUser, PermissionsMixin):
    phone_number = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=20, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_venue_owner = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, blank=True, null=True)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
