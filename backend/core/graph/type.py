from graphene_django import DjangoObjectType


class SmartDjangoObjectType(DjangoObjectType):
    class Meta:
        abstract = True

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        fields=None,
        **options,
    ):
        cls_fields = set(
            cls._meta.fields.keys()
        )
        try:
            fields.extend(cls_fields)
        except Exception:
            pass
        return super().__init_subclass_with_meta__(
            fields=fields,
            **options,
        )
