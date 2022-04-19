from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response

# Create your views here.
from apps.appointments.models import AppointmentDay
from apps.appointments.serializers import TimeSlotSerializer, AppointmentSerializer
from apps.appointments.utils import get_appointment_day
from apps.user_app.utils import get_doctor_object


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
