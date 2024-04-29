from django.contrib import admin
from .models import Specialty, MedicalData, OpenDate

admin.site.register(Specialty)
admin.site.register(MedicalData)
admin.site.register(OpenDate)