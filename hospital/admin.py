from django.contrib import admin
from .models import Appointment
from .models import Medicine, Patient, Visit, TestResult



# Register your models here.
admin.site.register(Appointment)
admin.site.register(Medicine)
admin.site.register(Patient)
admin.site.register(Visit)
admin.site.register(TestResult)
