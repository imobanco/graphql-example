from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from ..models import Todo, TodoItem
from .serializers import TodoItemSerializer, TodoSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoItemViewSet(ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


router = DefaultRouter()
router.register("todos", TodoViewSet, basename="todos_rest")
router.register("todo_itens", TodoViewSet, basename="todo_itens_rest")

urlpatterns = router.urls
