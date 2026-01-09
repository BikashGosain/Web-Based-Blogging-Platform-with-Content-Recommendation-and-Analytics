from django.urls import path
from .import views

urlpatterns = [
    # Dashboard Home
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.catagories, name='categories'),  # Example additional URL
    path('categories/add/', views.add_category, name='add_category'),  # Example additional URL
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),
]