from django.db import models

# Create your models here.
class Mbti(models.Model):

    MBTI_CHOICES = {
        ('INFP', 'INFP'),
        ('ENFP', 'ENFP'),
        ('ESFJ', 'ESFJ'),
        ('ISFJ', 'ISFJ'),
        ('ISFP', 'ISFP'),
        ('ESFP', 'ESFP'),
        ('INTP', 'INTP'),
        ('INFJ', 'INFJ'),
        ('ENFJ', 'ENFJ'),
        ('ENTP', 'ENTP'),
        ('ESTJ', 'ESTJ'),
        ('ISTJ', 'ISTJ'),
        ('INTJ', 'INTJ'),
        ('ISPT', 'ISTP'),
        ('ESTP', 'ESTP'),
        ('ENTJ', 'ENTJ'),
    }

    BOARD_CHOICES = {
        ('상대법', '상대법'),
        ('주의할 점', '주의할 점'),
        ('특징', '특징'),
    }

    board = models.CharField(max_length=50, choices=BOARD_CHOICES, null=False)
    character = models.CharField(max_length=50, null=False)
    summary = models.CharField(max_length=200, null=False)
    mbti = models.CharField(max_length=50, choices=MBTI_CHOICES, null=False)
    title = models.CharField(max_length=200)
    content = models.TextField()