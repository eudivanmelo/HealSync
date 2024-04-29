from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from apps.doctor.models import MedicalData

class MyLoginMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.error(self.request, 'Você precisa estar logado para acessar esta página.')
        return super().handle_no_permission()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if MedicalData.objects.filter(user=self.request.user).exists():
            context["medical_data"] = MedicalData.objects.get(user=self.request.user)
            
        return context