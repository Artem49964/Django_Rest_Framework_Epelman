from rest_framework import serializers

from .managers import AutoParkManager
from .models import AutoParkModel


class AutoParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'created_at', 'updated_at')

        