from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from .utils import upload_rg, upload_medical_identity, upload_photo

class Specialty(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class MedicalData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.DO_NOTHING)
    crm = models.CharField(max_length=15, blank=False, null=False)

    # Address
    cep = models.CharField(max_length=15, blank=False, null=False)
    street = models.CharField(max_length=100, blank=False, null=False)
    neighborhood = models.CharField(max_length=100, blank=False, null=False)
    number = models.CharField(max_length=10, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)

    # Documents Files
    rg = models.ImageField(upload_to=upload_rg)
    medical_identity = models.ImageField(upload_to=upload_medical_identity)
    photo = models.ImageField(upload_to=upload_photo)

    # Others
    description = models.TextField()
    value = models.FloatField(default=100)

    def __str__(self):
        return f'Dr./Dra {self.user.first_name} {self.user.last_name}'
    
    @property
    def next_date(self):
        next_date = OpenDate.objects.filter(user=self.user)
        next_date = next_date.filter(date__gt=timezone.now()).filter(scheduled=False)
        next_date = next_date.order_by('date').first()
        if next_date:   
            return next_date.date.strftime('%Y-%m-%d %H:%M')
        else:
            return 'Indisponível'
    
class OpenDate(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scheduled = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.date}'
    