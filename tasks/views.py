from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Task
from .serializers import TaskSerializer
from django.conf import settings
from django.http import JsonResponse
from utils.authentication import validate_api_key

@api_view(['POST'])
def create_task(request):
    if not validate_api_key(request):
        return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    
    if not request.data:
        return Response({'error': 'Empty request body'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print(f"Error al crear la tarea: {e}")
        return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def list_tasks(request):
    if not validate_api_key(request):
        return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        tasks = Task.objects.all()
        
        if not tasks.exists():
            return Response({'message': 'No tasks available'}, status=status.HTTP_204_NO_CONTENT)
        
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        print(f"Error al obtener las tareas: {e}")
        return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_task(request, task_id):
    if not validate_api_key(request):
        return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        task = Task.objects.get(pk=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        print(f"Error al obtener la tarea con ID {task_id}: {e}")  # Log del error
        return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['PUT'])
def update_task(request, task_id=None):
    if not validate_api_key(request):
        return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    
    if not request.data:
        return Response({'error': 'Empty request body'}, status=status.HTTP_400_BAD_REQUEST)
    
    if task_id is None:
        return Response({'error': 'Task ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        task = Task.objects.get(pk=task_id)

    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        print(f"Error al actualizar la tarea con ID {task_id}: {e}")  # Log del error
        return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_task(request, task_id=None):
    if not validate_api_key(request):
        return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    if task_id is None:
        return Response({'error': 'Task ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        task = Task.objects.get(task_id=task_id)
        task.delete()
        return Response({'message': 'Task deleted'}, status=status.HTTP_204_NO_CONTENT)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        print(f"Error al eliminar la tarea con ID {task_id}: {e}")  # Log del error
        return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)