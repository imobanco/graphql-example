from django.db import models
from core.models import BaseModel


class Todo(BaseModel):
    class Meta:
        ordering = ["created_at"]
        verbose_name = "Lista de Tarefas"
        verbose_name_plural = "Listas de Tarefas"

    name = models.CharField(max_length=255, verbose_name="nome", help_text="nome da lista")


class TodoItem(BaseModel):
    class Meta:
        ordering = ["created_at"]
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    name = models.CharField(max_length=255, verbose_name="nome", help_text="nome da tarefa")
    done = models.BooleanField(default=False)
    todo = models.ForeignKey(to=Todo, on_delete=models.PROTECT, related_name='itens')
