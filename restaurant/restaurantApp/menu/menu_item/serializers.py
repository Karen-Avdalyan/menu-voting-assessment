from rest_framework import serializers

from restaurant.restaurantApp.menu.menu_item.models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, min_length=1, max_length=255)
    description = serializers.CharField(required=False, max_length=4095)
    price = serializers.FloatField(required=True)

    def create(self, validated_data):
        menu_item = MenuItem.objects.create(
            name=validated_data['name'],
            manager=validated_data['description']
        )
        menu_item.save()
        return menu_item

    class Meta:
        model = MenuItem
        fields = ('id', 'name', 'description', 'price')
