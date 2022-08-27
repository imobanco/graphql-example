from core.views.graph_type import BaseModelObjectType

from ..models import Person


class PersonType(BaseModelObjectType):
    class Meta:
        model = Person
        fields = ["name"]
