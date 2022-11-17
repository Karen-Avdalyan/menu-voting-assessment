from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from restaurant.restaurantApp.permissions import IsAuthorizedForRestaurant
from restaurant.restaurantApp.restaurant.models import Restaurant
from restaurant.restaurantApp.restaurant.serializers import CreateRestaurantSerializer, AlterRestaurantSerializer


class ListCreateRestaurantAPIView(ListCreateAPIView):
    serializer_class = CreateRestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [IsAuthorizedForRestaurant]


class RetrieveUpdateDestroyRestaurantAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AlterRestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [IsAuthorizedForRestaurant]
