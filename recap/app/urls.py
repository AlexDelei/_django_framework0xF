from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='default-page'),
    path('home/', views.home, name='homepage'),
    path('home/details/<int:id>', views.details, name='details-page')
]