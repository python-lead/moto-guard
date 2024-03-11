from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from src.apps.motorcycle.models import Motorcycle, MotorcycleBrand
from src.apps.motorcycle.mongo_models import MotorcycleDetails
from src.apps.motorcycle.serializers import (
    MongoMotorcycleDetailsSerializer,
    MotorcycleBrandSerializer,
    MotorcycleSerializer,
)
from src.mongodb.utils import MongoViewSetMixin


class MotorcycleBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MotorcycleBrand.objects.all()
    serializer_class = MotorcycleBrandSerializer


class MotorcycleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Motorcycle.objects.all()
    serializer_class = MotorcycleSerializer


class MotorcycleDetailMongoViewSet(
    MongoViewSetMixin,
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
):
    model = MotorcycleDetails
    serializer_class = MongoMotorcycleDetailsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = self.model(**serializer.validated_data)
        instance.save()

        return Response(instance.dict(), status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=kwargs.pop("partial", False)
        )
        serializer.is_valid(raise_exception=True)

        self.model(**{**instance.dict(), **serializer.validated_data})

        instance.update(data=serializer.validated_data)

        return Response(instance.dict())
