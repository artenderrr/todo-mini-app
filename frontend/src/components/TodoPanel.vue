<script setup>
import { ref, onMounted } from "vue";
import TodoFilter from "./TodoFilter.vue";
import TodoAddButton from "./TodoAddButton.vue";
import Todo from "./Todo.vue";

const isHidden = ref(true);

function slideIn() {
  setTimeout(() => isHidden.value = false, 1);
}

onMounted(slideIn);
</script>

<template>
  <div class="panel" :class="{ hidden: isHidden }">
    <div class="controls-wrapper">
      <TodoFilter />
      <TodoAddButton />
    </div>
    <div class="todos-wrapper">
    <Todo />
    <Todo />
    <Todo />
    </div>
  </div>
</template>

<style scoped>
.panel {
  background-color: #2b2b2b;

  width: 40rem;
  max-width: 100%;
  height: 80%;

  display: flex;
  flex-direction: column;
  gap: 1rem;

  border: .125rem solid #3b3b3b;
  border-bottom: none;
  border-top-left-radius: 2rem;
  border-top-right-radius: 2rem;

  padding: 2rem;
  margin: auto;

  transition: transform 1s;
}

.panel.hidden {
  transform: translateY(100%);
}

.controls-wrapper {
  width: 100%;
  height: 12.5%;

  display: flex;
  justify-content: space-between;
}

.todos-wrapper {
  display: flex;
  flex-direction: column;
  gap: 1rem;

  overflow: scroll;
}

.todos-wrapper::-webkit-scrollbar {
  display: none;
}
</style>