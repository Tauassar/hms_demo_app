from django.urls import path, include
from apps.appointments.views import AppointmentDayView, Appointments

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('<int:doctor_pk>/<str:date>', AppointmentDayView.as_view()),
    path('', Appointments.as_view()),
]
