from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import create_task, list_tasks, get_task, update_task, delete_task

urlpatterns = [
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/', list_tasks, name='list_tasks'),
    path('tasks/<int:task_id>/', get_task, name='get-task'),
    path('tasks/update/<int:task_id>/', update_task, name='update_task'), 
    path('tasks/delete/<int:task_id>/', delete_task, name='delete_task'),
]