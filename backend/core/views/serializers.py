from ..models import BaseModel

from ..rest_framework.serializers import SmartModelSerializer


class BaseModelSerializer(SmartModelSerializer):
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
        extra_kwargs = {
            "id": {"read_only": True},
            "minimal_id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "resource_type": {"read_only": True},
            "verbose_name": {"read_only": True},
            "verbose_name_plural": {"read_only": True},
        }
