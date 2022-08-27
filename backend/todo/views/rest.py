from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter
from .serializers import TodoSerializer, TodoItemSerializer
from ..models import Todo, TodoItem


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
