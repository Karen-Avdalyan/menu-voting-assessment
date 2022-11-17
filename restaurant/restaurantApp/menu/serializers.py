from rest_framework import serializers

from restaurant.restaurantApp.menu.menu_item.models import MenuItem
from restaurant.restaurantApp.menu.menu_item.serializers import MenuItemSerializer
from restaurant.restaurantApp.menu.models import Menu
from restaurant.restaurantApp.restaurant.models import Restaurant
from restaurant.restaurantApp.restaurant.serializers import RestaurantSerializer


class CreateMenuSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    date = serializers.DateField(required=True)
    items = MenuItemSerializer(many=True, required=True)
    restaurant_id = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Restaurant.objects.all(),
        write_only=True,
    )
    restaurant = RestaurantSerializer(read_only=True)

    def create(self, validated_data):
        menu = Menu.objects.create(
            name=validated_data['name'],
            date=validated_data['date'],
            restaurant=validated_data['restaurant_id']
        )
        items = validated_data.pop('items')
        for item in items:
            MenuItem.objects.create(**item, menu=menu)

        menu.save()
        return menu

    class Meta:
        model = Menu
        fields = ('id', 'name', 'date', 'items', 'restaurant', 'restaurant_id')


class AlterMenuSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    date = serializers.DateField(required=False)
    items = MenuItemSerializer(many=True, required=False)
    restaurant_id = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Restaurant.objects.all(),
    )

    def update(self, instance, validated_data):
        items = validated_data.pop('items', [])
        if items:
            old_items = instance.items
            for old_item in old_items.all():
                old_item.delete()
            for item in items:
                MenuItem.objects.create(**item, menu=instance)
        return super().update(instance, validated_data)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'date', 'items', 'restaurant_id')


class MenuVoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    date = serializers.DateField(required=True)
    items = MenuItemSerializer(many=True, required=True)
    restaurant = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Restaurant.objects.all(),
    )
    score = serializers.FloatField(required=True)
