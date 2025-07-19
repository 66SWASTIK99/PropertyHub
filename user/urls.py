from django.urls import path
from .import views

urlpatterns = [
    path('api/signup/', views.UserSignUpAPIView.as_view(), name='signupapi'),
    path('api/login/', views.UserLogInAPIView.as_view(),name='loginapi'),
    path('api/forgetpw/',views.ForgetpwAPI.as_view(),name='forgetpwapi')
]