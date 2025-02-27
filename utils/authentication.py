from django.conf import settings

# Función para verificar API Key
def validate_api_key(request):
    api_key = request.headers.get('API-KEY')
    return api_key == settings.API_KEY