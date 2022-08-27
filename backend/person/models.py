from django.db import models

from core.models import BaseModel


class Person(BaseModel):
    class Meta:
        ordering = ["created_at"]
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    name = models.CharField(max_length=255, verbose_name="nome", help_text="nome completo")
