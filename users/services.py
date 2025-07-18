from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

def login_user_raw(user_data):
    email = user_data.get("email")
    password  = user_data.get("password")
    sql = "SELECT password FROM users WHERE email = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, [email])
        user = cursor.fetchone()

    if user:
        stored_hashed_password = user[0]
        if check_password(password, stored_hashed_password):
            return Response({"message": "Login successful."}, status=200)
        else:
            return Response({"error": "Incorrect password."}, status=401)
    else:
        return Response({"error": "User not found."}, status=404)
    
def signup_user_raw(user_data):
    hashed_password = make_password(user_data.get("password"))
    sql = """
        INSERT INTO users 
        (username, email, password)
        VALUES (%s, %s, %s)
    """
    values = (
        user_data.get("username"),
        user_data.get("email"),
        hashed_password,
    )
    with connection.cursor() as cursor:
        cursor.execute(sql, values)