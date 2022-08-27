from ..models import Person
from core.views.graph_type import BaseModelObjectType


class PersonType(BaseModelObjectType):
    class Meta:
        model = Person
        fields = ["name"]
