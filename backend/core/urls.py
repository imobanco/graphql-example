from rest_framework.routers import DefaultRouter

from .apis.rest import HealthCheckViewSet, ImobancoServicesViewSet

router = DefaultRouter()
router.register("health_check", HealthCheckViewSet, basename="health_check")
router.register(
    "imobanco_services", ImobancoServicesViewSet, basename="imobanco_services"
)

urlpatterns = router.urls
