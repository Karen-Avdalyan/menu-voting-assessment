import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from restaurant.restaurantApp.menu.models import Menu
from restaurant.restaurantApp.menu.vote.models import SCORE_CHOICES, Vote
from restaurant.restaurantApp.user.employee.models import Employee


class VoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Employee.objects.all(),
    )
    menu = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Menu.objects.all(),
    )
    score = serializers.ChoiceField(choices=SCORE_CHOICES)

    def create(self, validated_data):
        return Vote.objects.create(
            menu=validated_data['menu'],
            score=validated_data['score'],
            user=self.context['request'].user.employee,
        )

    class Meta:
        model = Vote
        fields = ('id', 'score', 'user', 'menu')


class ThreeVotesSerializer(serializers.Serializer):
    menus = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Menu.objects.all(),
        write_only=True,
        many=True,
    )

    def validate_menus(self, menus):
        if len(menus) != 3:
            raise ValidationError("Menu count should be 3")
        for menu in menus:
            if menu.date != datetime.date.today():
                raise ValidationError("Menu dates should be current day")
        return menus
