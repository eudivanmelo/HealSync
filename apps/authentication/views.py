from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import CreateUserForm

class Login(LoginView):
    template_name = 'login.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Nome de usuário ou senha incorretos.')
        return super().form_invalid(form)

class Register(FormView):
    template_name = 'register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Cadastro efetuado com sucesso.')
        return super().form_valid(form)

class ForgotPassword(PasswordResetView):
    template_name = 'password.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Email não encontrado.')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, f"Email enviado para {form.cleaned_data['email']}")
        return redirect(reverse_lazy('login'))
    
    

def logout_view(request):
    logout(request)
    messages.success(request, 'Deslogado com sucesso!')
    return redirect(reverse_lazy('login'))