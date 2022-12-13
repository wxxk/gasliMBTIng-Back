from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "community"

urlpatterns = [
    path("", views.community_list),
    path("create/", views.community_create),
    path("<int:pk>/", views.community_detail),
    path("update/<int:pk>/", views.community_update),
    path("delete/<int:pk>/", views.community_delete),
    path("<int:community_pk>/comment/", views.comment_list),
    path("<int:community_pk>/comment/create/", views.comment_create),
    path("<int:community_pk>/comment/delete/<int:comment_pk>/", views.comment_delete),
    path("recomment/", views.recomment_list),
    path(
        "<int:community_pk>/comment/<int:comment_pk>/recomment/create/",
        views.recomment_create,
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
