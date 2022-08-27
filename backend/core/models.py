import uuid

from django.contrib.contenttypes.models import ContentType
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True

    @property
    def minimal_id(self):
        return str(self.id)[:8]

    @classmethod
    def get_verbose_name(cls):
        # noinspection PyProtectedMember,PyUnresolvedReferences
        return cls._meta.verbose_name

    @property
    def verbose_name(self):
        return self.get_verbose_name()

    @classmethod
    def get_verbose_name_plural(cls):
        # noinspection PyProtectedMember,PyUnresolvedReferences
        return cls._meta.verbose_name_plural

    @property
    def verbose_name_plural(self):
        return self.get_verbose_name_plural()

    @classmethod
    def get_content_type(cls):
        return ContentType.objects.get_for_model(cls)

    @property
    def content_type(self):
        return self.get_content_type()

    @property
    def resource_type(self):
        # noinspection PyUnresolvedReferences
        return self._meta.object_name
