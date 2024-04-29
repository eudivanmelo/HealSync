from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class CreateUserForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password_confirm']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Esse email já está em uso.')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Esse nome de usuário já está em uso.')
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        password_confirm = cleaned_data.get('password_confirm')

        if cleaned_data.get('password') and password_confirm and password_confirm != cleaned_data.get('password'):
            raise ValidationError('As senhas não coincidem.')

        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        
        return user