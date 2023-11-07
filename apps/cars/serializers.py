from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'auto_park_id', 'brand', 'price', 'year', 'body', 'created_at', 'updated_at')

    def validate(self, attrs):
        price = attrs.get('price')
        year = attrs.get('year')
        if price == year:
            raise serializers.ValidationError({r'details':'price value can\'t be like year'})
        return super().validate(attrs)



