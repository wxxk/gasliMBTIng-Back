from django.urls import path
from . import views

app_name = 'friends'

urlpatterns = [
    path('', views.friends_list),
    # path('filter/<str:filter>', views.friends_filter),
    path('filter/', views.friends_filter),
    path('create/', views.friends_create),
    path('get/<int:pk>/', views.friends_get),
    path('<int:pk>/', views.friends_detail),
    path('update/<int:pk>/', views.friends_update),
    path('delete/<int:pk>/', views.friends_delete),
    path('mygroups/', views.groups_list),
    path('mygroups/create/', views.groups_create),
    path('mygroups/delete/<int:pk>/', views.groups_delete),
]