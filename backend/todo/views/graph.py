import graphene
from graphene_django import DjangoListField
from graphene_django.rest_framework.mutation import SerializerMutation

from .graph_type import TodoType, TodoItemType
from .rest_serializers import TodoSerializer, TodoItemSerializer


class TodoMutation(SerializerMutation):
    class Meta:
        serializer_class = TodoSerializer


class TodoQuery(graphene.ObjectType):
    todos_list = DjangoListField(TodoType)
    todos_write = TodoMutation.Field()


class TodoItemMutation(SerializerMutation):
    class Meta:
        serializer_class = TodoItemSerializer


class TodoItemQuery(graphene.ObjectType):
    todo_itens_list = DjangoListField(TodoItemType)
    todo_itens_write = TodoItemMutation.Field()
