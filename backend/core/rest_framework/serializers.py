from rest_framework import serializers


class SmartModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        mro = self.__class__.mro()
        mro.reverse()
        # Reverter o MRO garante que as PONTAS da
        # árvore possam sobreescrever os extra_kwargs

        fields = set()
        extra_kwargs = dict()

        for cls in mro:
            try:
                fields.update(cls.Meta.fields)
            except AttributeError:
                pass

            try:
                extra_kwargs.update(cls.Meta.extra_kwargs)
            except AttributeError:
                pass

        self.Meta.fields = list(fields)
        self.Meta.extra_kwargs = extra_kwargs
