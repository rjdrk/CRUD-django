from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import create_task

urlpatterns = [
    path('tasks/create/', create_task, name='create_task'),
    #path('<int:task_id>/', views.get_task, name='get_task'),
    #path('<int:task_id>/update/', views.update_task, name='update_task'),
    #path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
]