from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.departments.models import Departments
from apps.user_app.models import UserContacts, DoctorFields, MedicalStatus


class Command(BaseCommand):
    department_data = [
        {
            "title": "Хирургия",
            "sub_title": "Sample subtitle",
            "link": "/department/surgery"
        },
        {
            "title": "Кардиология",
            "sub_title": "Sample subtitle",
            "link": "/department/cardio"
        },
        {
            "title": "Педиатрия",
            "sub_title": "Sample subtitle",
            "link": "/departments"
        },
        {
            "title": "Sample",
            "sub_title": "Sample subtitle",
            "link": "/departments"
        },
        {
            "title": "Sample",
            "sub_title": "Sample title",
            "link": "/departments"
        },
        {
            "title": "Sample",
            "sub_title": "Sample subtitle",
            "link": "/departments"
        }
    ]

    user_data = [
        {
            "username": "970112541136",
            "first_name": "Иван",
            "last_name": "Иванов",
            "password": "1223",
            "type": "doctor",
            "position": "Хирург кардиолог",
            "education": "Медицинский университет, Астана",
            "experience": "Городская больница №6 (1993-1997)",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
            "contacts": {
                "email": "doctor@email.com",
                "telephone": "87777777777",
                "address": "Doctor str. 1"
            },
            "short_description": "Hello, I\"m a test doctor",
            "img": "1.png"
        },
        {
            "username": "admin1",
            "password": "1223",
            "first_name": "Тамерлан",
            "last_name": "Шамелов",
            "birth_date": "05.07.1999",
            "type": "patient",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
            "contacts": {
                "address": "Кабанбай батыра, 55",
                "email": "patient@email.com",
                "telephone": "87777777778"
            },
            "medical_status": {
                "status": "Здоров",
                "blood_group": "A+",
                "vaccination_status": "Вакцинирован",
                "allergies": "Новокаин, Аспирин"
            },
        }
    ]

    def create_department_data(self):
        for department in self.department_data:
            Departments.objects.create(
                title=department['title'],
                sub_title=department['sub_title'],
                link=department['link']
            )

    def create_users(self):
        with transaction.atomic():
            department = Departments.objects.get(id=1)
            userModel = get_user_model()
            for user_data in self.user_data:
                user = userModel.objects.create_user(
                    username=user_data['username'],
                    type=user_data['type'],
                    description=user_data['description'],
                    password=user_data['password'],
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name']
                )
                contacts = user_data['contacts']
                UserContacts.objects.create(
                    user=user,
                    telephone=contacts['telephone'],
                    email=contacts['email'],
                    address=contacts['address']
                )
                if user_data['type'] == 'doctor':
                    DoctorFields.objects.create(
                        user=user,
                        education=user_data['education'],
                        position=user_data['position'],
                        experience=user_data['experience'],
                        department=department,
                        short_description=user_data['short_description'],
                        img=user_data['img'],
                    )
                else:
                    med_status = user_data['medical_status']
                    MedicalStatus.objects.create(
                        user=user,
                        status=med_status['status'],
                        blood_group=med_status['blood_group'],
                        vaccination_status=med_status['vaccination_status'],
                        allergies=med_status['allergies'],
                    )

    def handle(self, **options):
        print("TEST DATA FILL Process initiated")
        userModel = get_user_model()
        userModel.objects.create_user(
            username=970113351179,
            type='doctor',
            password='1223',
            is_superuser=1
        )
        self.create_department_data()
        self.create_users()
        print("TEST DATA FILL Process finished")
