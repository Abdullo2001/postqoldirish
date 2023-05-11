from django.urls import path
from .views import HomePageView,PostDetailView,PostCreateView,PostUpdateView

urlpatterns = [
    path('post/new/',PostCreateView.as_view(),name="post_create"),
    path('post/<int:pk>/',PostDetailView.as_view(),name="post_detail"),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name="post_update"),
    path('',HomePageView.as_view(),name="home"),
]
