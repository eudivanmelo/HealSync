from django.views.generic import CreateView, ListView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils import timezone
from .models import MedicalData, OpenDate
from healsync.utils import MyLoginMixin

class medical_register(MyLoginMixin, CreateView):
    model = MedicalData
    template_name = "medical_register.html"
    fields = ['specialty','crm','cep','street',
              'neighborhood','number','city','rg',
              'medical_identity','photo','description','value']
    success_url = reverse_lazy('open_date')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if MedicalData.objects.filter(user=request.user).exists():
                messages.warning(request, 'Você já possui cadastro médico!')
                return redirect(reverse_lazy('open_date'))
            
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Cadastro médico realizado com sucesso!')
        return super().form_valid(form)
    
class open_date(MyLoginMixin, CreateView, ListView):
    model = OpenDate
    template_name = "open_date.html"
    fields = ['date']
    context_object_name = 'dates'
    success_url = reverse_lazy('open_date')
    
    def form_valid(self, form):
        if form.instance.date <= timezone.now():
            messages.warning(self.request, 'Você não pode adicionar uma horário anterior ao horário atual!')
            return redirect(reverse_lazy('open_date'))

        form.instance.user = self.request.user
        messages.success(self.request, 'Adicionado um novo horário de atendimento!')
        return super().form_valid(form)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not MedicalData.objects.filter(user=request.user).exists():
                messages.error(request, 'Apenas médicos podem abrir horário, realize seu cadastro médico!')
                return redirect(reverse_lazy('medical_register'))
        
        return super().dispatch(request, *args, **kwargs)