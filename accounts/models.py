from django.db import models
from django.contrib.auth.models import AbstractUser

# import bcrypt


class User(AbstractUser):
    nickname = models.CharField(max_length=30)

    # 성별
    남 = "남"
    여 = "여"
    CHOICES_gender = ((남, "남"), (여, "여"))
    gender = models.CharField(max_length=25, choices=CHOICES_gender, default=남)

    # MBTI
    E = "E"
    I = "I"
    N = "N"
    S = "S"
    T = "T"
    F = "F"
    P = "P"
    J = "J"

    CHOICES_mbti1 = ((E, "E"), (I, "I"))
    CHOICES_mbti2 = ((N, "N"), (S, "S"))
    CHOICES_mbti3 = ((T, "T"), (F, "F"))
    CHOICES_mbti4 = ((P, "P"), (J, "J"))
    mbti1 = models.CharField(max_length=25, choices=CHOICES_mbti1, default=E)
    mbti2 = models.CharField(max_length=25, choices=CHOICES_mbti2, default=N)
    mbti3 = models.CharField(max_length=25, choices=CHOICES_mbti3, default=T)
    mbti4 = models.CharField(max_length=25, choices=CHOICES_mbti4, default=P)

    age = models.IntegerField(null=True)
    image = models.ImageField(upload_to="media/account_images/", blank=True, null=True)
