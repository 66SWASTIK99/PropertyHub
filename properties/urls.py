from django.urls import path
from .import views

urlpatterns = [
    path('addproperties/', views.AddNewPropertyAPIView.as_view(), name='addpropertiesapi'),
]