from django.urls import path
from .views import PatientView, ScheduleView

urlpatterns = [
    path('', PatientView.as_view(), name='patient'),
    path('schedule_time/<int:doctor_id>', ScheduleView.as_view(), name='schedule_time')
]
