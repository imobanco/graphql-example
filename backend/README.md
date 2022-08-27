# Backend

Esse é um backend feito com Django + DRF + Graphene!

## Graphql

Exemplo de query graphql
```

{
  personsList{
    id,
    name
  }
  personWrite: personsWrite(input:{name: "Foo Bar"}) {
    id,
    name
  }
  personUpdate: personsWrite(input:{name: "Foo Bar", id: "5ea23c62-f9d3-45ad-9781-27c9f2de84f6"}) {
    id,
    name
  }
  todosList{
    id,
    name
  }
  todoItensList{
    id,
    name,
    done, 
    todo{
      id, 
      name
    }
  }
  todoWrite: todosWrite(input:{name: "Meu todo list"}){
    id, 
    name
  }
  todoUpdate: todosWrite(input:{name: "Meu todo list atualizado", id:"11e3096c-ef41-421c-bb1b-e13789c0a66f"}){
    id, 
    name
  }
  todoItemWrite: todoItensWrite(input:{name:"Meu item todo", done: false, todo:"11e3096c-ef41-421c-bb1b-e13789c0a66f"}){
    id, name, done, todo
  }
  todoItemUpdate: todoItensWrite(input:{name:"Meu item todo atualizado", id:"ef4cb418-ed35-4c9f-857b-4bb0368d3bdf", todo:"11e3096c-ef41-421c-bb1b-e13789c0a66f"}){
    id, name, done, todo
  }
}

```