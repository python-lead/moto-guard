from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from src.apps.motorcycle.views import (
    MotorcycleBrandViewSet,
    MotorcycleDetailMongoViewSet,
    MotorcycleViewSet,
)

app_name = "motorcycle"

router = DefaultRouter()
router.register(r"brands", MotorcycleBrandViewSet, basename="brands")

motorcycle_router = routers.NestedSimpleRouter(router, r"brands", lookup="motorcycle")
motorcycle_router.register(r"motorcycles", MotorcycleViewSet, basename="models")

motorcycle_detail_router = routers.NestedSimpleRouter(
    motorcycle_router, r"motorcycles", lookup="motorcycle_mongo_details"
)
motorcycle_detail_router.register(
    r"details", MotorcycleDetailMongoViewSet, basename="mongo_moto"
)

urlpatterns = router.urls + motorcycle_router.urls + motorcycle_detail_router.urls
