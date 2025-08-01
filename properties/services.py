from django.db import connection
from rest_framework.response import Response
from datetime import datetime

def add_new_property_raw(data, user_id):
    
    property_type = data.get('property_type')
    location = data.get('location')
    contact_number = data.get('contact_number')
    listed_by_user_id = user_id
    # = data.get('')
    if not property_type or not location or not contact_number or not listed_by_user_id:
        return Response({"error": "Necessary fields are not filled."}, status=400)

    # current datetime to store datetime during listing
    now = datetime.now()

    sql = """
        INSERT INTO properties 
        (property_type, location, contact_number, listed_date_time, listed_by_user_id, 
        monthly_rent, deposit_amount, property_description)
        VALUES (%s, %s, %s, %s, %s,
                %s, %s, %s)
    """
    values = (property_type, location, contact_number, now, listed_by_user_id,
            data.get('monthly_rent'),
            data.get('deposit_amount', 0),
            data.get('property_description') 
            )

    with connection.cursor() as cursor:
        cursor.execute(sql, values)
    connection.commit()
    
    return Response({"message": "New property added succesfully"}, status=201)