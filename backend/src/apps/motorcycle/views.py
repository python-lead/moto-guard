from rest_framework import viewsets

from src.apps.motorcycle.models import Motorcycle, MotorcycleBrand
from src.apps.motorcycle.serializers import (
    MotorcycleBrandSerializer,
    MotorcycleSerializer,
)


class MotorcycleBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MotorcycleBrand.objects.all()
    serializer_class = MotorcycleBrandSerializer


class MotorcycleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Motorcycle.objects.all()
    serializer_class = MotorcycleSerializer
