from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)