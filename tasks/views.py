from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Task
from .serializers import TaskSerializer
from django.conf import settings
from django.http import JsonResponse

# Middleware de autenticación por API Key
# Función para verificar API Key
def validate_api_key(request):
    api_key = request.headers.get('API-KEY')
    return api_key == settings.API_KEY

@api_view(['POST'])
def create_task(request):
    if not validate_api_key(request):
        return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)