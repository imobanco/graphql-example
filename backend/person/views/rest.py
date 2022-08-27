from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from ..models import Person
from .serializers import PersonSerializer


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


router = DefaultRouter()
router.register("persons", PersonViewSet, basename="persons_rest")

urlpatterns = router.urls
