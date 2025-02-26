from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get("API-KEY")
        if not api_key or api_key != settings.API_KEY:
            raise AuthenticationFailed("Invalid API Key")
        return (None, None)