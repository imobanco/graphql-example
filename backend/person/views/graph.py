import graphene
from graphene_django import DjangoListField
from graphene_django.rest_framework.mutation import SerializerMutation

from .graph_type import PersonType
from .rest_serializers import PersonSerializer


class PersonMutation(SerializerMutation):
    class Meta:
        serializer_class = PersonSerializer


class PersonQuery(graphene.ObjectType):
    persons_list = DjangoListField(PersonType)
    persons_write = PersonMutation.Field()
