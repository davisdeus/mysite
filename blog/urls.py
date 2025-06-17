from django.urls import path

from blog import views

urlpatterns = [
    path("", views.PostView.as_view(), name="home"),
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
]
