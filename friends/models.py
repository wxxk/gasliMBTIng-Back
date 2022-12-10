from django.db import models
from django.conf import settings

# Create your models here.
class Friend(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=100)
    mbti = models.CharField(max_length=100)
    grade = models.CharField(max_length=10, null=True)
    group = models.CharField(max_length=100, null=True)

class Group(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=100)