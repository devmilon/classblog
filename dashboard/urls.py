from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard'),
    path('posts/', views.dashboard_home, name='dashboard_posts'),
    path('create/', views.create_post, name='create_post'),
]