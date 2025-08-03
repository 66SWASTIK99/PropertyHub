from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.db import connection
from .services import signup_user_raw, login_user_raw
from django.contrib.auth.hashers import make_password


@api_view(['POST'])
@permission_classes([AllowAny])
def user_signup_view(request):
    username=request.data.get('username')
    email=request.data.get('email')
    password=request.data.get('password')
    
    if not username or not email or not password:
        return Response({"error": "All fields are required."}, status=400)
        
    return signup_user_raw(request.data)


@api_view(['GET'])
@permission_classes([AllowAny])       
def user_login_view(request):
    email=request.data.get('email')
    password=request.data.get('password')

    if not email or not password:
        return Response({"error": "All fields are required."}, status=400)

    return login_user_raw(request.data)
    
class ForgetpwAPI(APIView):
    def post(self, request):
        password = request.data.get('password')
        email = request.data.get('email')
        hashed_password = make_password(password)
        conn = connection()
        cursor = conn.cursor()


        # Update the password
        cursor.execute("UPDATE users SET password = %s WHERE email = %s", [hashed_password, email])
        conn.commit()
        conn.close()

        return Response({"message": "Password changed successfully"}, status=200)
    