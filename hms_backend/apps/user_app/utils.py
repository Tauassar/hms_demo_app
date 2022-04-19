from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist


def get_doctor_object(doctor_pk):
    try:
        return get_user_model().objects.get(
            username=doctor_pk
        )
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist("Врач не найден")
