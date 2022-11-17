from django.urls import path

from restaurant.restaurantApp.restaurant.views import ListCreateRestaurantAPIView, \
    RetrieveUpdateDestroyRestaurantAPIView

urlpatterns = [
    path('<int:pk>', RetrieveUpdateDestroyRestaurantAPIView.as_view()),
    path('', ListCreateRestaurantAPIView.as_view(), name="restaurant"),
]
