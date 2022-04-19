from rest_framework import serializers
from .models import Departments


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'
