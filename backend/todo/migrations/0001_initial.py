# Generated by Django 4.1 on 2022-08-27 14:01

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="nome da lista", max_length=255, verbose_name="nome"
                    ),
                ),
            ],
            options={
                "verbose_name": "Lista de Tarefas",
                "verbose_name_plural": "Listas de Tarefas",
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="TodoItem",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="nome da tarefa", max_length=255, verbose_name="nome"
                    ),
                ),
                ("done", models.BooleanField(default=False)),
                (
                    "todo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="itens",
                        to="todo.todo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tarefa",
                "verbose_name_plural": "Tarefas",
                "ordering": ["created_at"],
            },
        ),
    ]
