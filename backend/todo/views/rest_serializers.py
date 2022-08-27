from core.views.rest_serializers import BaseModelSerializer

from ..models import Todo, TodoItem


class TodoSerializer(BaseModelSerializer):
    class Meta:
        model = Todo
        fields = [
            "name",
        ]
        extra_kwargs = {}


class TodoItemSerializer(BaseModelSerializer):
    class Meta:
        model = TodoItem
        fields = ["name", "done", "todo"]
        extra_kwargs = {}
