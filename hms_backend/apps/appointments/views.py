from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime


# Create your views here.
from apps.appointments.models import AppointmentDay
from apps.appointments.serializers import AppointmentDaySerializer


def isWeekend(date):
    return True if datetime.fromisoformat(date).weekday() > 4\
        else False


class AppointmentDayView(APIView, RetrieveAPIView):
    queryset = AppointmentDay.objects.all()
    serializer_class = AppointmentDaySerializer

    # def get_serializer_class(self)
    #     if self.action == 'list':
    #         return self.serializer_classes['listSerializer']
    #     if self.action == 'retrieve':
    #         return self.serializer_classes['retrieveSerializer']

    def retrieve(self, request, *args, **kwargs):
        staff = self.get_object().staff.all().prefetch_related('user')
        users = [x.user for x in staff]
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
