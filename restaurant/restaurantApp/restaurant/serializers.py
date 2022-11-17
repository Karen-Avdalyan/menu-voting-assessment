from rest_framework import serializers

from restaurant.restaurantApp.restaurant.models import Restaurant
from restaurant.restaurantApp.user.restaurant_manager.models import RestaurantWorker


class RestaurantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    manager = serializers.PrimaryKeyRelatedField(required=True, many=False, queryset=RestaurantWorker.objects.all())

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'manager')


class CreateRestaurantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    manager = serializers.PrimaryKeyRelatedField(required=True, many=False, queryset=RestaurantWorker.objects.all())

    def validate_name(self, value):
        try:
            Restaurant.objects.get(name=value)
            raise serializers.ValidationError("Restaurant with this name exists")
        except Restaurant.DoesNotExist:
            return value

    def create(self, validated_data):
        restaurant = Restaurant.objects.create(
            name=validated_data['name'],
            manager=validated_data['manager']
        )
        restaurant.save()
        return restaurant

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'manager')


class AlterRestaurantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    manager = serializers.PrimaryKeyRelatedField(required=True, many=False, queryset=RestaurantWorker.objects.all())

    def validate_name(self, value):
        if self.instance.name != value:
            try:
                Restaurant.objects.get(name=value)
                raise serializers.ValidationError("Restaurant with this name exists")
            except Restaurant.DoesNotExist:
                return value
        return value

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'manager')
