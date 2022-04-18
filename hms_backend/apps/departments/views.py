from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from apps.departments.models import Departments
from apps.departments.serializers import DepartmentListSerializer
from apps.user_app.serializers import DepartmentDoctorsSerializer


class DepartmentList(viewsets.ReadOnlyModelViewSet):
    queryset = Departments.objects.all()
    serializer_classes = {
        'listSerializer': DepartmentListSerializer,
        'retrieveSerializer': DepartmentDoctorsSerializer
    }

    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializer_classes['listSerializer']
        if self.action == 'retrieve':
            return self.serializer_classes['retrieveSerializer']

    def retrieve(self, request, *args, **kwargs):
        staff = self.get_object().staff.all().prefetch_related('user')
        users = [x.user for x in staff]
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
