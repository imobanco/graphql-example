<script setup lang="ts">
import TheWelcome from "@/components/TheWelcome.vue";
import {BakcendHttpAdaptor} from "@/core/adapters/http_backend"
import {PersonRepository} from "@/person/repository"

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

</script>

<template>
  <main>
    <button @click='myCall'>Me aperte</button>
    <TheWelcome />
  </main>
</template>
