from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.user_detail),
    path('edit/', views.user_edit),
    path('delete/', views.user_delete),
]