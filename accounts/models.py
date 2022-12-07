from django.db import models
from django.contrib.auth.models import AbstractUser

# import bcrypt

class User(AbstractUser):
    # username = models.CharField(unique=True, max_length=50)
    # password = models.CharField(max_length=128)

    nickname = models.CharField(max_length=30)    
    mbti1 = models.CharField(null=True, max_length=1)
    mbti2 = models.CharField(null=True, max_length=1)
    mbti3 = models.CharField(null=True, max_length=1)
    mbti4 = models.CharField(null=True, max_length=1)
    gender = models.CharField(null=True, max_length=1)
    age = models.IntegerField(null=True)