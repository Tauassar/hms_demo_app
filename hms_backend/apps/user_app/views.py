from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse

# Create your views here.
from rest_framework import status, views
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.user_app.models import CustomUser, MedicalHistory
from apps.user_app.serializers import GetDoctorSerializer, CreateDoctorSerializer, \
    GetPatientSerializer, CreatePatientSerializer, CreateMedicalHistorySerializer


def logoutView(request):
    logout(request)
    return HttpResponse({"status": "success"})


class LoginView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                if request.user.type == 'doctor':
                    serializer = GetDoctorSerializer(request.user)
                elif request.user.type == 'patient':
                    serializer = GetPatientSerializer(request.user)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            else:
                return Response(
                    status=status.HTTP_404_NOT_FOUND,
                    data={"status": "check provided data"}
                )
        else:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"status": "check provided data"}
            )


class DoctorViewSet(ModelViewSet):
    queryset = CustomUser.objects.filter(type=CustomUser.UserType[0][0])
    serializer_classes = {
        'default': GetDoctorSerializer,
        'create': CreateDoctorSerializer,
    }

    def get_serializer_class(self):
        if self.action == 'create':
            return self.serializer_classes[self.action]
        return self.serializer_classes['default']


class PatientViewSet(ModelViewSet):
    queryset = CustomUser.objects.filter(type=CustomUser.UserType[1][0])
    serializer_classes = {
        'default': GetPatientSerializer,
        'create': CreatePatientSerializer,
    }

    def get_serializer_class(self):
        if self.action == 'create':
            return self.serializer_classes[self.action]
        return self.serializer_classes['default']


class MedicalHistoryView(
    CreateModelMixin,
    GenericAPIView):
    allowed_methods = ['POST']
    queryset = MedicalHistory.objects.all()
    serializer_class = CreateMedicalHistorySerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
