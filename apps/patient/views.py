from django.views.generic import ListView
from healsync.utils import MyLoginMixin
from apps.doctor.models import MedicalData, Specialty, OpenDate
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone

class PatientView(MyLoginMixin, ListView):
    model = MedicalData
    template_name = "home.html"
    context_object_name = "doctors"

    def get_queryset(self):
        queryset = super().get_queryset()

        name_filter = self.request.GET.get('search')
        if name_filter:
            queryset = (queryset.filter(user__first_name__icontains=name_filter) | 
                        queryset.filter(user__last_name__icontains=name_filter))

        specialty_filter = self.request.GET.getlist('specialty') 
        if specialty_filter:
            queryset = queryset.filter(specialty_id__in=specialty_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["specialtys"] = Specialty.objects.all()
        return context
    
class ScheduleView(MyLoginMixin, ListView):
    model = OpenDate
    template_name = "schedule.html"
    context_object_name = "dates"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.kwargs.get('doctor_id'):
            if not MedicalData.objects.filter(user_id=self.kwargs.get('doctor_id')).exists():
                messages.error(self.request, 'Médico não encontrado no banco de dados.') 
            else:
                context['doctor'] = MedicalData.objects.get(user_id=self.kwargs.get('doctor_id'))

        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_id=self.kwargs.get('doctor_id'))
        queryset = queryset.filter(date__gt=timezone.now())
        return queryset
    

    
