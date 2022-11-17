from django.urls import path
from restaurant.restaurantApp.user.employee.views import RetrieveUpdateDestroyEmployeeAPIView, ListCreateEmployeeAPIView
from restaurant.restaurantApp.user.restaurant_manager.views import RetrieveUpdateDestroyRestaurantWorkerAPIView, \
    ListCreateRestaurantWorkerAPIView

urlpatterns = [
    path('employee/<int:pk>', RetrieveUpdateDestroyEmployeeAPIView.as_view(), name="user-employee-detail"),
    path('employee/', ListCreateEmployeeAPIView.as_view(), name="user-employee"),

    path('restaurant-worker/<int:pk>', RetrieveUpdateDestroyRestaurantWorkerAPIView.as_view(), name="user-restaurant-worker"),
    path('restaurant-worker/', ListCreateRestaurantWorkerAPIView.as_view(), name="user-restaurant-worker"),
]
