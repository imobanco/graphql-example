from core.views.rest_serializers import BaseModelSerializer

from ..models import Person


class PersonSerializer(BaseModelSerializer):
    class Meta:
        model = Person
        fields = [
            "name",
        ]
        extra_kwargs = {}
