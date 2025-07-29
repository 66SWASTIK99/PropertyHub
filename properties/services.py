from django.db import connection
from rest_framework.response import Response
from datetime import datetime

def add_new_property_raw(data):
    now = datetime.now()

    property_type = data.get('property_type')
    location = data.get('location')
    contact_number = data.get('contact_number')
    listed_by_user_id = data.get('listed_by_user_id')
    # = data.get('')
    if not property_type or not location or not contact_number or not listed_by_user_id:
        return Response({"error": "Necessary fields are not filled."}, status=400)

    sql = """
        INSERT INTO properties 
        (property_type, location, contact_number, listed_date_time, listed_by_user_id, 
        rent_amount, deposit_amount, property_description)
        VALUES (%s, %s, %s, %s,
                %s, %s, %s)
    """
    values = (property_type, location, contact_number, now, listed_by_user_id,
            data.get('rent_amount'),
            data.get('deposit_amount', 0),
            data.get('property_description') 
            )

    with connection.cursor() as cursor:
        cursor.execute(sql, values)
    
    return Response({"message": "New property added succesfully"}, status=201)