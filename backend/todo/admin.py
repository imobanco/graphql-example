from django.contrib import admin

from .models import Todo, TodoItem


admin.site.register(Todo)
admin.site.register(TodoItem)
