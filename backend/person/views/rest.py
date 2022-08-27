from rest_framework.viewsets import ModelViewSet

from rest_framework.routers import DefaultRouter
from .serializers import PersonSerializer
from ..models import Person


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


router = DefaultRouter()
router.register("persons", PersonViewSet, basename="persons_rest")

urlpatterns = router.urls
