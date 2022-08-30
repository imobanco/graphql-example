<script setup lang="ts">
import TheWelcome from "@/components/TheWelcome.vue";
import {BakcendHttpAdaptor} from "@/core/adapters/http_backend"
import {PersonRepository} from "@/person/repository"
import { GraphQuery, GraphRequest, GrapModelAdapter } from "@/core/adapters/graph_model";

const myCall = async () => {
  console.log('my call')
  const repo = new PersonRepository()
  let person = repo.get_empty_entity()
  person.name = 'Meu nome'
  await repo.create(person)
  console.log('create', person)
  person.name = 'Meu nome alterado de teste'
  await repo.update(person)
  console.log('update', person)
}

const myCall2 = async () => {
  const r = new GraphRequest(
    [
      new GraphQuery('query', ['a', 'b'], {'a': 1, 'b': 2}, 'nome'),
      new GraphQuery('query', ['a', 'b'], undefined, 'nome2')
    ]
  )
  // console.log(r.constuct())

  const a = new GrapModelAdapter('personsList', 'personsRetrieve', 'personsWrite', ['id', 'name'])
  console.log(await a.create({'name': 'Graph Request Front'}))
  console.log(await a.list())
  console.log(await a.list(['id'], 'meu_read'))
}

</script>

<template>
  <main>
    <button @click='myCall'>Me aperte</button>
    <button @click='myCall2'>Me aperte 2</button>
    <TheWelcome />
  </main>
</template>
