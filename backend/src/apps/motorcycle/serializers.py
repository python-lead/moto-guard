from rest_framework import serializers

from src.apps.motorcycle.models import Motorcycle, MotorcycleBrand


class MotorcycleBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotorcycleBrand
        fields = (
            "id",
            "name",
            "country_of_origin",
            "year_established",
        )


class MotorcycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = (
            "id",
            "brand",
            "displacement",
            "drive_type",
            "model",
            "short_description",
            "type",
            "year",
        )


class MotorcycleDetailsSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    motorcycle_id = serializers.IntegerField()
    model = serializers.CharField()
    year = serializers.IntegerField(min_value=1)
