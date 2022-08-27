from core.views.graph_type import BaseModelObjectType

from ..models import Todo, TodoItem


class TodoType(BaseModelObjectType):
    class Meta:
        model = Todo
        fields = ["name"]


class TodoItemType(BaseModelObjectType):
    class Meta:
        model = TodoItem
        fields = ["name", "done", "todo"]
