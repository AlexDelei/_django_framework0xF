from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
)


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #  page with a single post detail information. the pk stands for primary key
   path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
    path('details/<int:id>', views.details, name='blog-details'),
]