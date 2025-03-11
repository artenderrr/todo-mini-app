<script setup>
import Checkbox from "./Checkbox.vue";
import TodoInput from "./TodoInput.vue";
</script>

<template>
  <div class="card">
    <Checkbox />
    <TodoInput />
    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75zM20.71 7.04a.996.996 0 0 0 0-1.41l-2.34-2.34a.996.996 0 0 0-1.41 0l-1.83 1.83l3.75 3.75z"/></svg>
    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6zM19 4h-3.5l-1-1h-5l-1 1H5v2h14z"/></svg>
  </div>
</template>

<style scoped>
.card {
  background-color: #3b3b3b;

  width: 100%;
  min-height: 5rem;

  display: flex;
  justify-content: space-around;
  align-items: center;
  gap: 1rem;

  padding: 1rem;

  border: .125rem solid #4b4b4b;
  border-radius: 1rem;
}
</style>