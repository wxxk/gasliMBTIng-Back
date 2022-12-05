from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community_list),
    path('create/', views.community_create),
    path('<int:pk>/', views.community_detail),
    path('update/<int:pk>/', views.community_update),
    path('delete/<int:pk>/', views.community_delete),
    path('comment/', views.comment_list),
    path('<int:community_pk>/comment/create/', views.comment_create),
    path('recomment/', views.recomment_list),
    path('<int:community_pk>/comment/<int:comment_pk>/recomment/create/', views.recomment_create),
]