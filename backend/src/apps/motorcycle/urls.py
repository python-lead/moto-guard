from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from src.apps.motorcycle.views import (
    MotorcycleBrandViewSet,
    MotorcycleDetailMongoViewSet,
    MotorcycleViewSet,
)

app_name = "motorcycle"

router = DefaultRouter()
router.register("brands", MotorcycleBrandViewSet, basename="brands")
# todo: nest under motorcycle resource
router.register("mongo-moto", MotorcycleDetailMongoViewSet, basename="mongo_moto")

brand_router = routers.NestedDefaultRouter(router, "brands", lookup="brand")

brand_router.register("motorcycles", MotorcycleViewSet, basename="models")

urlpatterns = router.urls + brand_router.urls
