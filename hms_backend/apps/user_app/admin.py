from django.contrib import admin

# Register your models here.
from apps.user_app.models import CustomUser, UserContacts, DoctorFields, MedicalStatus, MedicalHistory

admin.site.register(CustomUser)
admin.site.register(UserContacts)
admin.site.register(DoctorFields)
admin.site.register(MedicalStatus)
admin.site.register(MedicalHistory)
