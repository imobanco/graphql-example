from graphene_django import DjangoObjectType


class SmartDjangoObjectType:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        mro = self.__class__.mro()
        mro.reverse()
        # Reverter o MRO garante que as PONTAS da
        # árvore possam sobreescrever os extra_kwargs

        fields = set()

        for cls in mro:
            try:
                fields.update(cls.Meta.fields)
            except AttributeError:
                pass

        self.Meta.fields = list(fields)
