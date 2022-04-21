from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from apps.appointments.models import Appointment, AppointmentDay
from apps.user_app.utils import get_doctor_object


class TimeSlotSerializer(serializers.Serializer):
    time_slot = serializers.CharField(
        max_length=12,
        read_only=True
    )


class GetAppointments(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        exclude = ['id']

    def create(self, validated_data):
        print(validated_data)
        doctor = validated_data.get('doctor')

        return Appointment.objects.create(
            time=validated_data.get('time'),
            description=validated_data.get('description'),
            patient=validated_data.get('patient'),
            doctor=doctor,
            date=validated_data.get('date')
        )
