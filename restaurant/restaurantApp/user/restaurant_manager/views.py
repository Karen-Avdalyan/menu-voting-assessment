from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser

from restaurant.restaurantApp.user.restaurant_manager.models import RestaurantWorker
from restaurant.restaurantApp.user.restaurant_manager.serializers import AlterRestaurantWorkerSerializer, \
    CreateRestaurantWorkerSerializer


class ListCreateRestaurantWorkerAPIView(ListCreateAPIView):
    serializer_class = CreateRestaurantWorkerSerializer
    queryset = RestaurantWorker.objects.all()
    permission_classes = [IsAdminUser]


class RetrieveUpdateDestroyRestaurantWorkerAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AlterRestaurantWorkerSerializer
    queryset = RestaurantWorker.objects.all()
    permission_classes = [IsAdminUser]
