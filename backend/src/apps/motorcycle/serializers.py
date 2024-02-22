from rest_framework.serializers import ModelSerializer
from src.apps.motorcycle.models import Motorcycle, MotorcycleBrand


class MotorcycleBrandSerializer(ModelSerializer):
    class Meta:
        model = MotorcycleBrand
        fields = (
            "id",
            "name",
            "country_of_origin",
            "year_established",
        )


class MotorcycleSerializer(ModelSerializer):
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
