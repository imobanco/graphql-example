import graphene

from person.views.graph import PersonQuery
from todo.views.graph import TodoQuery, TodoItemQuery

queries = (PersonQuery, TodoQuery, TodoItemQuery)


Query = type("Query", queries, {})


schema = graphene.Schema(query=Query)
