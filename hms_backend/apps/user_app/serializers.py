import traceback

from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.departments.models import Departments
from apps.user_app.models import CustomUser, DoctorFields, UserContacts, MedicalStatus, MedicalHistory


class UserContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContacts
        exclude = ['user']


def create_user_and_contacts(validated_data):
    userModel = get_user_model()
    user = userModel.objects.create_user(
        username=validated_data['username'],
        type=validated_data['type'],
        description=validated_data['description'],
        password=validated_data['password'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name']
    )
    contacts = validated_data.get('contacts')
    UserContacts.objects.create(
        user=user,
        telephone=contacts['telephone'],
        email=contacts['email'],
        address=contacts['address']
    )
    return user

# DOCTOR SERIALIZERS


class GetDoctorSerializer(serializers.ModelSerializer):
    contacts = UserContactsSerializer()
    department_str = serializers.ReadOnlyField(
        source='get_user_department'
    )
    position = serializers.SlugRelatedField(
        queryset=DoctorFields.objects.all(),
        source='doctor',
        slug_field='position'
     )
    education = serializers.SlugRelatedField(
        queryset=DoctorFields.objects.all(),
        source='doctor',
        slug_field='education'
     )
    experience = serializers.SlugRelatedField(
        queryset=DoctorFields.objects.all(),
        source='doctor',
        slug_field='experience'
     )
    department = serializers.SlugRelatedField(
        queryset=DoctorFields.objects.all(),
        source='doctor',
        slug_field='department_id'
     )
    short_description = serializers.SlugRelatedField(
        queryset=DoctorFields.objects.all(),
        source='doctor',
        slug_field='short_description'
     )
    img = serializers.SlugRelatedField(
        queryset=DoctorFields.objects.all(),
        source='doctor',
        slug_field='img'
     )

    class Meta:
        model = CustomUser
        exclude = [
            'password',
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions'
        ]


class CreateDoctorSerializer(GetDoctorSerializer):
    position = serializers.CharField(max_length=50, write_only=True)
    education = serializers.CharField(max_length=50, write_only=True)
    experience = serializers.CharField(max_length=50, write_only=True)
    department = serializers.SlugRelatedField(
        queryset=Departments.objects.all(),
        slug_field='id',
        write_only=True
    )
    short_description = serializers.CharField(
        max_length=50,
        allow_blank=True,
        write_only=True
    )
    img = serializers.CharField(
        max_length=50,
        allow_blank=True,
        write_only=True
    )

    def create(self, validated_data):
        user = create_user_and_contacts(validated_data)
        DoctorFields.objects.create(
            user=user,
            education=validated_data.get('education'),
            position=validated_data.get('position'),
            experience=validated_data.get('experience'),
            department=validated_data.get('department'),
            short_description=validated_data.get('short_description'),
            img=validated_data.get('img'),
        )
        return user

    class Meta:
        model = CustomUser
        exclude = [
            'is_superuser',
            'last_login',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions'
        ]


class DepartmentDoctorsSerializer(serializers.ModelSerializer):
    description_short = serializers.SlugRelatedField(
        queryset=DoctorFields.objects.all(),
        source='doctor',
        slug_field='short_description',
    )
    img = serializers.SlugRelatedField(
        queryset=DoctorFields.objects.all(),
        source='doctor',
        slug_field='img',
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'description_short', 'img']


# PATIENT SERIALIZERS


class MedicalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalStatus
        exclude = ['user', 'id']


class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        exclude = ['user', 'id']


class CreateMedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'


class GetPatientSerializer(serializers.ModelSerializer):
    contacts = UserContactsSerializer()
    medical_status = MedicalStatusSerializer()
    medical_history = MedicalHistorySerializer(many=True)

    class Meta:
        model = CustomUser
        exclude = [
            'password',
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions'
        ]


class CreatePatientSerializer(GetPatientSerializer):
    class Meta:
        model = CustomUser
        exclude = [
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions'
        ]

    def create(self, validated_data):
        print(validated_data)
        user = create_user_and_contacts(validated_data)
        med_status = validated_data.get('medical_status')
        MedicalStatus.objects.create(
            user=user,
            status=med_status['status'],
            blood_group=med_status['blood_group'],
            vaccination_status=med_status['vaccination_status'],
            allergies=med_status['allergies'],
        )
        return user
