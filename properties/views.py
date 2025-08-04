from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import request
from django.db import connection
from .services import add_new_property_raw
from users.jwt import TokenManager
from users.auth import JWTAuthentication

class AddNewPropertyAPIView(APIView):
    def post(self, request):
        #auth_header = request.META.get('HTTP_AUTHORIZATION')
        
        jwt = JWTAuthentication()
        token_payload = jwt.authenticate(request)
        
        if token_payload is None:
            # Token is invalid or expired
            return Response({"error": "Invalid or expired token"}, status=401)
        
        # Extracting user_id from token payload
        user_id = token_payload.get("user_id")

        return add_new_property_raw(request.data, user_id)