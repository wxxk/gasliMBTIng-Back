from django.db import models

# Create your models here.
class Mbti(models.Model):
    board = models.IntegerField()
    mbti = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content= models.TextField()