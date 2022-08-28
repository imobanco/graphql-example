<script setup lang="ts">
import TheWelcome from "@/components/TheWelcome.vue";
import {BakcendHttpAdaptor} from "@/core/adapters/http_backend"
import {PersonRepository} from "@/person/repository"

const myCall = async () => {
  console.log('my call')
  const repo = new PersonRepository()
  let person = await repo.create('Meu Nome teste')
  console.log('create', person)
  person.name = 'Meu nome alterado de teste'
  person = await repo.update_entity(person)
  console.log('update entity', person)
  person = await repo.update_data(person.id, {'name': 'Meu nome alterado sem entity de teste'})
  console.log('update entity', person)
}

</script>

<template>
  <main>
    <button @click='myCall'>Me aperte</button>
    <TheWelcome />
  </main>
</template>
