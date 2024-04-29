from .views import medical_register, open_date
from django.urls import path

urlpatterns = [
   path('register/', medical_register.as_view(), name='medical_register'),
   path('open_date/', open_date.as_view(), name='open_date')
]