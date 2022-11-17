from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser

from restaurant.restaurantApp.user.employee.models import Employee
from restaurant.restaurantApp.user.employee.serializers import CreateEmployeeSerializer, AlterEmployeeSerializer


class ListCreateEmployeeAPIView(ListCreateAPIView):
    serializer_class = CreateEmployeeSerializer
    queryset = Employee.objects.all()
    # permission_classes = [IsAdminUser]


class RetrieveUpdateDestroyEmployeeAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AlterEmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAdminUser]

