from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User, Group


class CreateEmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=8, max_length=255)

    def validate_username(self, value):
        try:
            User.objects.get(username=value)
            raise serializers.ValidationError("User with this username exists")
        except User.DoesNotExist:
            return value

    def create(self, validated_data):
        employee = Employee.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        employee_group = Group.objects.first()
        employee_group.user_set.add(employee)
        employee.save()
        return employee

    class Meta:
        model = Employee
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')


class AlterEmployeeSerializer(serializers.ModelSerializer):
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
        model = Employee
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')
