from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.response import Response

# Create your views here.
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from apps.appointments.models import AppointmentDay, Appointment
from apps.appointments.serializers import TimeSlotSerializer, AppointmentSerializer, GetAppointments
from apps.appointments.utils import get_appointment_day
from apps.user_app.utils import get_doctor_object


class Appointments(
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    allowed_methods = ['GET']
    queryset = Appointment.objects.all()
    serializer_class = GetAppointments
    permission_classes = []
    authentication_classes = []


class AppointmentDayView(
    RetrieveModelMixin,
    CreateModelMixin,
    GenericAPIView
):
    allowed_methods = ['GET', 'POST']
    queryset = AppointmentDay.objects.all()
    serializer_classes = {
        'create': AppointmentSerializer,
        'retrieve': TimeSlotSerializer,
    }
    permission_classes = []
    authentication_classes = []

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_classes['retrieve']
        return self.serializer_classes['create']

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        date = self.kwargs['date']
        doctor_pk = self.kwargs['doctor_pk']

        try:
            doctor = get_doctor_object(doctor_pk)
            appointment_day = get_appointment_day(date, doctor)
            if appointment_day:
                time_slots = appointment_day.get_available_time_slots()
            else:
                time_slots = AppointmentDay.get_all_time_slots()
            serializer = self.get_serializer(time_slots, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        doctor_pk = self.kwargs['doctor_pk']

        try:
            doctor = get_doctor_object(doctor_pk)

            if not AppointmentDay.objects.filter(
                    date=self.kwargs['date'],
                    doctor=doctor
            ).exists():
                day = AppointmentDay.objects.create(
                    date=self.kwargs['date'],
                    doctor=doctor
                ).save()
            else:
                day = AppointmentDay.objects.get(
                    date=self.kwargs['date'],
                    doctor=doctor
                )
            serializer = self.get_serializer(
                data=request.data,
                context={
                    'date': day
                }
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        except ObjectDoesNotExist as e:
            return Response({
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
