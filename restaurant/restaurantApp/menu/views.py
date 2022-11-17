import datetime
from functools import reduce

from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from restaurant.restaurantApp.menu.models import Menu
from restaurant.restaurantApp.menu.serializers import CreateMenuSerializer, AlterMenuSerializer, MenuVoteSerializer
from restaurant.restaurantApp.menu.vote.serializers import VoteSerializer, ThreeVotesSerializer
from restaurant.restaurantApp.permissions import IsAuthorizedForMenuListCreation, IsAuthorizedForMenuVoting, \
    IsAuthorizedForMenuAlter


class ListCreateMenuAPIView(ListCreateAPIView):
    serializer_class = CreateMenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [IsAuthorizedForMenuListCreation]


class RetrieveUpdateDestroyMenuAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AlterMenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [IsAuthorizedForMenuAlter]


class TodaysMenuAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateMenuSerializer

    def get(self, request):
        menus = Menu.objects.filter(date=datetime.date.today())

        page = self.paginate_queryset(menus)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(menus, many=True)
        return Response(serializer.data)


class CreateMenuVoteAPIView(GenericAPIView):
    permission_classes = [IsAuthorizedForMenuVoting]
    serializer_class = ThreeVotesSerializer

    def post(self, request):
        if 'Build-Version' in request.headers and request.headers['Build-Version'] == '1.0.0':
            response = self.vote_old_way(request)
        else:
            response = self.vote_new_way(request)
        request.user.employee.last_voted = datetime.date.today()
        request.user.employee.save()
        return response

    def vote_new_way(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        score = 3
        created_votes = []
        for m in serializer.validated_data['menus']:
            data = {
                "menu": m.id,
                "score": score
            }
            serializer = VoteSerializer(data=data, context=self.get_serializer_context())
            serializer.is_valid(raise_exception=True)
            serializer.save()
            created_votes.append(serializer.data)
            score -= 1
        return Response(created_votes, status=status.HTTP_201_CREATED)

    def vote_old_way(self, request):
        request.data['score'] = '3'
        serializer = VoteSerializer(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TodayVotes(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateMenuSerializer

    def get(self, request):
        menus = Menu.objects.filter(date=datetime.date.today())

        for menu in menus:
            votes = reduce(lambda x, y: x + int(y.score), menu.votes.all(), 0)
            menu.__setattr__('score', votes)

        serializer = MenuVoteSerializer(menus, many=True)
        return Response(serializer.data)
