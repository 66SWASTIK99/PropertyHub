from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from .services import add_new_property_raw

class AddNewPropertyAPIView(APIView):
    def post(self, request):
        return add_new_property_raw(request.data)


