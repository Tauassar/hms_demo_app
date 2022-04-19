from django.db import models

from apps.user_app.models import CustomUser


class AppointmentDay(models.Model):
    class Meta:
        db_table = 'appointment_day'

    doctor = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='appointment_day'
    )
    date = models.DateField(
        unique=True,
        primary_key=True
    )

    def get_available_time_slots(self):
        appointment_list = self.appointment_event.all()
        time_slot_list = [x for _, x in Appointment.TimeSlots.choices]
        time_slots = []

        for appointment in appointment_list:
            time_slot_list.remove(Appointment.get_time_string(appointment.time))

        for time_slot in time_slot_list:
            time_slots.append({
                "time_slot": time_slot
            })
        return time_slots

    @staticmethod
    def get_all_time_slots():
        time_slots = []
        for _, time_slot in Appointment.TimeSlots.choices:
            time_slots.append({
                "time_slot": time_slot
            })
        return time_slots

    def __str__(self):
        return f'{self.doctor.first_name} {self.doctor.last_name} {self.date}'


class Appointment(models.Model):
    class TimeSlots(models.IntegerChoices):
        NINE = 1, '9:00-9:30'
        NINE_HALF = 2, '9:30-10:00'
        TEN = 3, '10:00-10:30'
        TEN_HALF = 4, '10:30-11:00'
        ELEVEN = 5, '11:00-11:30'
        ELEVEN_HALF = 6, '11:30-12:00'
        TWELVE = 7, '12:00-12:30'
        TWELVE_HALF = 8, '12:30-13:00'
        FOURTEEN_HALF = 9, '14:30-15:00'
        FIFTEEN = 10, '15:00-15:30'
        FIFTEEN_HALF = 11, '15:00-15:30'
        SIXTEEN = 12, '16:00-16:30'
        SIXTEEN_HALF = 13, '16:30-17:00'
        SEVENTEEN = 14, '17:00-17:30'
        SEVENTEEN_HALF = 15, '17:30-18:00'

    class Meta:
        db_table = 'patient_appointments'

    patient = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='appointment'
    )
    doctor = models.ForeignKey(
        CustomUser,
        related_name='appointments_list',
        on_delete=models.CASCADE
    )
    date = models.ForeignKey(
        AppointmentDay,
        on_delete=models.CASCADE,
        related_name='appointment_event'
    )
    time = models.IntegerField(choices=TimeSlots.choices)
    description = models.CharField(max_length=200)

    @classmethod
    def get_time_string(cls, time_int):
        for num, string in cls.TimeSlots.choices:
            if num == time_int:
                return string
        return None

    @classmethod
    def get_time_int(cls, time_str):
        for num, string in cls.TimeSlots.choices:
            if string == time_str:
                return int
        return None

    def __str__(self):
        return f'{self.date} ' \
               f'{self.get_time_string(self.time)}'


class UpcomingAppointments(models.Model):
    class Meta:
        db_table = 'patient_upcoming_appointments'

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    last_appointment = models.DateField()
    upcoming_appointment = models.DateField()
