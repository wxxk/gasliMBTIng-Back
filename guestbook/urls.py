from django.urls import path
from . import views

app_name = 'guestbook'

urlpatterns = [
    path('', views.guestbook_list),
    # path('filter/<str:filter>', views.guestbook_filter),
    # path('filter/', views.guestbook_filter),
    path('create/', views.guestbook_create),
    path('<int:pk>/', views.guestbook_detail),
    # path('update/<int:pk>/', views.guestbook_update),
    path('delete/<int:pk>/', views.guestbook_delete),
]