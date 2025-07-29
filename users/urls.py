from django.urls import path
from .import views

urlpatterns = [
    path('signup/', views.UserSignUpAPIView.as_view(), name='signupapi'),
    path('login/', views.UserLogInAPIView.as_view(),name='loginapi'),
    path('forgetpw/',views.ForgetpwAPI.as_view(),name='forgetpwapi')
]