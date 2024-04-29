from django.urls import path
from .views import Login, Register, logout_view, ForgotPassword

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('forgot_password/', ForgotPassword.as_view(), name='forgot_password')
]