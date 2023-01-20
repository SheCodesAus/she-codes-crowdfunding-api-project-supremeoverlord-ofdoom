from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    def __str__(self):   #when you ask for a string of something it will return this)
        return self.username

# Create your models here.
