import graphene

from person.views.graph import PersonQuery

queries = (PersonQuery,)


Query = type("Query", queries, {})


schema = graphene.Schema(query=Query)
