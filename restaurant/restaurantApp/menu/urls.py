from django.urls import path
from restaurant.restaurantApp.menu.views import ListCreateMenuAPIView, RetrieveUpdateDestroyMenuAPIView, \
    TodaysMenuAPIView, CreateMenuVoteAPIView, TodayVotes

urlpatterns = [
    path('', ListCreateMenuAPIView.as_view(), name="menu"),
    path('today', TodaysMenuAPIView.as_view()),
    path('<int:pk>', RetrieveUpdateDestroyMenuAPIView.as_view()),
    path('vote', CreateMenuVoteAPIView.as_view(), name="vote"),
    path('today/vote', TodayVotes.as_view())
]
