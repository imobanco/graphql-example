from ..graph.type import SmartDjangoObjectType
from ..models import BaseModel


class BaseModelObjectType(SmartDjangoObjectType):
    class Meta:
        model = BaseModel
        fields = [
            "id",
            "minimal_id",
            "created_at",
            "updated_at",
            "resource_type",
            "verbose_name",
            "verbose_name_plural",
        ]
