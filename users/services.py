from django.db import connection
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .jwt import TokenManager

def login_user_raw(user_data):
    email = user_data.get("email")
    password  = user_data.get("password")

    with connection.cursor() as cursor:
        cursor.execute("SELECT user_id, password FROM users WHERE email = %s", [email])
        user = cursor.fetchone()

    if not user:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)

    user_id, stored_hashed_password = user

    if not check_password(password, stored_hashed_password):
        return JsonResponse({'error': 'Invalid credentials'}, status=401)

    # Password is correct
            
    # Generating tokens
    token_manager = TokenManager()
    tokens = token_manager.generate_tokens(user_id)
            
    return JsonResponse({
        'message': 'Login successful',
        'user_id': user_id,
        "refresh_token": tokens['refresh_token'],
        "access_token": tokens['access_token'],
        "expires_in": tokens['expires_in']
        },
        status=200)
            
    # if user:
    #     stored_hashed_password = user[0]
    #     if check_password(password, stored_hashed_password):
    #         return Response({"message": "Login successful."}, status=200)
    #     else:
    #         return Response({"error": "Incorrect password."}, status=401)
    # else:
    #     return Response({"error": "User not found."}, status=404)
    

def signup_user_raw(user_data):
    email = user_data.get("email")
    sql = """SELECT email FROM users where email = %s"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [email])
        check_email = cursor.fetchone()

    if(check_email):
        return Response({"error": "Email already exists."}, status=409)
       
    username = user_data.get("username")
    hashed_password = make_password(user_data.get("password"))

    sql = """
        INSERT INTO users 
        (username, email, password)
        VALUES (%s, %s, %s) RETURNING user_id
    """
    values = (
        username,
        email,
        hashed_password,
    )
    with connection.cursor() as cursor:
        cursor.execute(sql, values)
        user_id = cursor.fetchone()[0]
    connection.commit()

    token_manager = TokenManager(connection)
    tokens = token_manager.generate_tokens(user_id)

    return Response({"message": "User added successfully.",
                    "user_id": user_id,
                    "refresh_token": tokens['refresh_token'],
                    "access_token": tokens['access_token'],
                    "expires_in": tokens['expires_in']
                    },               
                    status=201)
        
    #except Exception as e:
    #    return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)