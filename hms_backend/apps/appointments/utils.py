from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist

from apps.appointments.models import AppointmentDay


def isWeekend(date):
    return True if datetime.fromisoformat(date).weekday() > 4 \
        else False


def get_appointment_day(date, doctor):
    try:
        return AppointmentDay.objects.get(
            doctor=doctor,
            date=date
        )
    except ObjectDoesNotExist:
        if isWeekend(date):
            raise ObjectDoesNotExist("На данную дату запись невозможна")
        else:
            return None


def create_appointment():
    pass
