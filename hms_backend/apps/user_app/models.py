from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from apps.departments.models import Departments


class CustomUser(AbstractUser):

    class Meta:
        db_table = 'users'

    UserType = (
        ('doctor', 'doctor'),
        ('patient', 'patient'),
        ('pharmacy', 'pharmacy'),
    )
    username = models.CharField(
        verbose_name=_('iin'),
        primary_key=True,
        unique=True,
        max_length=12,
        validators=[
            RegexValidator(r'^\d{12}$'),
            MinLengthValidator(12)
        ],
    )
    email = None
    type = models.CharField(_('user_type'), choices=UserType, max_length=8)
    description = models.TextField(_('description'))

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'type']

    objects = CustomUserManager()

    @property
    def get_user_department(self):
        if self.type == 'doctor':
            return self.doctor.department.title
        else:
            return ''

    def __str__(self):
        return f'{self.type} {self.first_name} {self.last_name}'


class UserContacts(models.Model):
    class Meta:
        db_table = 'user_contact_information'

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='contacts'
    )
    telephone = models.IntegerField()
    email = models.EmailField(_('email'), unique=True)
    address = models.CharField(max_length=50)


class DoctorFields(models.Model):

    class Meta:
        db_table = 'doctor_information'

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='doctor'
    )
    education = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    department = models.ForeignKey(
        Departments,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='staff'
    )
    short_description = models.CharField(max_length=50, null=True, blank=True, )
    img = models.CharField(max_length=50, null=True, blank=True)


class MedicalStatus(models.Model):

    class Meta:
        db_table = 'patient_medical_status'

    VaccinationStatusChoices = (
        ('Вакцинирован', 'Вакцинирован'),
        ('Не вакцинирован', 'Не вакцинирован'),
    )
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='medical_status'
    )
    status = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=2)
    vaccination_status = models.CharField(
        max_length=15,
        choices=VaccinationStatusChoices)
    allergies = models.CharField(max_length=100)


class MedicalHistory(models.Model):

    class Meta:
        db_table = 'patient_medical_history'

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='medical_history'
    )
    doctor = models.ManyToManyField(CustomUser, related_name='history_appointments')
    date = models.DateField()
    disease = models.CharField(max_length=200)
    treatment = models.CharField(max_length=200)

