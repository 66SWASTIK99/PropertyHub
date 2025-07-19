from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import get_connection
from .services import signup_user_raw
from .services import login_user_raw
from django.contrib.auth.hashers import make_password


class UserSignUpAPIView(APIView):
    def post(self, request):
        username=request.data.get('username')
        email=request.data.get('email')
        password=request.data.get('password')
        if not username or not email or not password:
            return Response({"error": "All fields are required."}, status=400)
        
        user_data = request.data
        try:
            signup_user_raw(user_data)
            return Response({"message": "User added successfully."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UserLogInAPIView(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')

        if not email or not password:
            return Response({"error": "All fields are required."}, status=400)
      
        data = request.data
        result = login_user_raw(data.get('email'), data.get('password'))
        return Response(result['body'], status=result['status'])
    
class ForgetpwAPI(APIView):
    def post(self, request):
        password = request.data.get('password')
        email = request.data.get('email')
        hashed_password = make_password(password)
        conn = get_connection()
        cursor = conn.cursor()


        # Update the password
        cursor.execute("UPDATE users SET password = %s WHERE email = %s", [hashed_password, email])
        conn.commit()
        conn.close()

        return Response({"message": "Password changed successfully"}, status=200)
    