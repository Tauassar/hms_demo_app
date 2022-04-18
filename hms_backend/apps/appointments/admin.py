from django.contrib import admin

# Register your models here.
from apps.appointments.models import AppointmentDay, Appointment

admin.site.register(AppointmentDay)
admin.site.register(Appointment)
