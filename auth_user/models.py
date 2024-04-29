from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=250)
    img = models.ImageField(upload_to='users/')
    region = models.CharField(max_length=250)


    def __str__(self) -> str:
        return self.username