from django.urls import path
from . import views

app_name = 'friends'

urlpatterns = [
    path('', views.friends_list),
    # path('filter/<str:filter>', views.friends_filter),
    path('filter/', views.friends_filter),
    path('create/', views.friends_create),
    path('<int:pk>/', views.friends_detail),
    path('update/<int:pk>/', views.friends_update),
    path('delete/<int:pk>/', views.friends_delete),
]