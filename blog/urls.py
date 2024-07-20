from django.urls import path
from blog.views import RegisterView, PostDetailAPIView, PostListCreateAPIView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('posts/', PostListCreateAPIView.as_view(), name="posts"),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name="post"),
]
