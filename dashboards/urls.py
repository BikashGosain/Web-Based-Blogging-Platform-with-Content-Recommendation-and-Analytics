from django.urls import path
from . import views

urlpatterns = [
    # Dashboard Home
    path('', views.dashboard, name='dashboard'),
    # Category crud
    path('categories/', views.catagories, name='categories'),  # Example additional URL
    path('categories/add/', views.add_category, name='add_category'),  # Example additional URL
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),

    # blog post crud
    path('posts/', views.posts, name='posts'),
    path('posts/add/', views.add_post, name='add_post'),
    path('posts/edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('posts/delete/<int:pk>/', views.delete_post, name='delete_post'),
    
    # users management by manager and admin through dashboard
    path('users/', views.users, name='users'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/edit/<int:pk>/', views.edit_user, name='edit_user'),
    path('users/delete/<int:pk>/', views.delete_user, name='delete_user'),
]