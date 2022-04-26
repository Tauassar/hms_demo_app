from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.appointments.views import AppointmentDayView, Appointments
from apps.user_app.views import MedicalHistoryView

router = DefaultRouter()
router.register(r'', Appointments, basename="appointments")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('<int:doctor_pk>/<str:date>', AppointmentDayView.as_view())
]
