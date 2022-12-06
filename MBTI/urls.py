from django.urls import path, include
from .views import mbti_list, mbti_details, mbti_create


urlpatterns = [
    path("", mbti_list),
    path("create/", mbti_create),
    path("<int:pk>/", mbti_details),
]
