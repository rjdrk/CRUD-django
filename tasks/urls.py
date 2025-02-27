from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import create_task, list_tasks,get_task

urlpatterns = [
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/', list_tasks, name='list_tasks'),
    path("tasks/<int:task_id>/", get_task, name="get-task"),
    #path('<int:task_id>/update/', views.update_task, name='update_task'),
    #path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
]