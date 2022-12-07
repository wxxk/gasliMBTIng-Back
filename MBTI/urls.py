from django.urls import path, include
from .views import mbti_list, mbti_details


urlpatterns = [
    path("", mbti_list),
    path("<int:pk>/", mbti_details),
]
