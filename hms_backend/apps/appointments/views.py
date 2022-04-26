from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework import filters

# Create your views here.
from apps.appointments.models import AppointmentDay, Appointment
from apps.appointments.serializers import TimeSlotSerializer, AppointmentSerializer, GetAppointments, PrescriptionSerializer
from apps.appointments.utils import get_appointment_day
from apps.user_app.utils import get_doctor_object
from apps.appointments import serializers


class Appointments(
    ListModelMixin,
    GenericAPIView
):
    allowed_methods = ['GET']
    queryset = Appointment.objects.all()
    serializer_class = GetAppointments

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


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
            })

    def create(self, request, *args, **kwargs):
        doctor_pk = self.kwargs['doctor_pk']

        try:
            doctor = get_doctor_object(doctor_pk)

            if not AppointmentDay.objects.filter(
                    date=request.data['date'],
                    doctor=doctor
            ).exists():
                AppointmentDay.objects.create(
                    date=request.data['date'],
                    doctor=doctor
                ).save()
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        except ObjectDoesNotExist as e:
            return Response({
                "error": str(e)
            })


class PrescriptionViewSet(
    ListModelMixin, 
    RetrieveModelMixin, 
    GenericViewSet):

    queryset = Appointment.objects.all()
    from rest_framework.permissions import AllowAny
    permission_classes = [AllowAny]
    serializer_class = PrescriptionSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['patient__first_name', 'doctor__first_name', 'date__date', 'medicine']

    def retrieve(self, request, *args, **kwargs):
        if request.user.type != 'pharmacy':
            return Response('this page is allowed only for pharmacists')
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if request.user.type != 'pharmacy':
            return Response('this page is allowed only for pharmacists')
        return super().list(request, *args, **kwargs)