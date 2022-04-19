from django.urls import path, include
from apps.appointments.views import AppointmentDayView

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('<int:doctor_pk>/<str:date>', AppointmentDayView.as_view()),
]
