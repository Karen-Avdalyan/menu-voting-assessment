"""
This is url file,
here you can give all urls of your project
"""
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
import restaurant.restaurantApp.user.urls as user_urls
import restaurant.restaurantApp.restaurant.urls as restaurant_urls
import restaurant.restaurantApp.menu.urls as menu_urls

schema_view = get_swagger_view(title='test')


urlpatterns = [
    path('api/v1/user/', include(user_urls)),
    path('api/v1/restaurant/', include(restaurant_urls)),
    path('api/v1/menu/', include(menu_urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
