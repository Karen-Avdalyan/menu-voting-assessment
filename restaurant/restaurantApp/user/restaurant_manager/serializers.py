from rest_framework import serializers
from .models import RestaurantWorker
from django.contrib.auth.models import User, Group


class CreateRestaurantWorkerSerializer(serializers.ModelSerializer):  # create class to serializer model
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=8, max_length=255)

    def validate_username(self, value):
        try:
            User.objects.get(username=value)
            raise serializers.ValidationError("User with this username exists")
        except User.DoesNotExist:
            return value

    def create(self, validated_data):
        restaurant_worker = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        restaurant_worker_group = Group.objects.last()
        restaurant_worker_group.user_set.add(restaurant_worker)

        return restaurant_worker

    class Meta:
        model = RestaurantWorker
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')


class AlterRestaurantWorkerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=8, max_length=255)

    def validate_username(self, value):
        if self.instance.username != value:
            try:
                User.objects.get(username=value)
                raise serializers.ValidationError("User with this username exists")
            except User.DoesNotExist:
                return value
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop('password'))
        super().update(instance, validated_data)
        return instance

    class Meta:
        model = RestaurantWorker
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')
