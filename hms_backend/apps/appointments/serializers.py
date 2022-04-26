from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from apps.appointments.models import Appointment, AppointmentDay
from apps.user_app.utils import get_doctor_object


class TimeSlotSerializer(serializers.Serializer):
    time_slot = serializers.CharField(
        max_length=12,
        read_only=True
    )
    id = serializers.IntegerField()


class GetAppointments(serializers.ModelSerializer):
    time_str = serializers.ReadOnlyField(
        source='get_own_time_string'
    )

    class Meta:
        model = Appointment
        exclude = ['time']


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        exclude = ['id', 'date']

    def create(self, validated_data):
        print(validated_data)
        doctor = validated_data.get('doctor')

        return Appointment.objects.create(
            time=validated_data.get('time'),
            description=validated_data.get('description'),
            patient=validated_data.get('patient'),
            doctor=doctor,
            date=self.context.get('date')
        )
