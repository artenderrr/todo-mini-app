<script setup>
import { ref, onMounted } from "vue";
import TodoFilter from "./TodoFilter.vue";
import TodoAddButton from "./TodoAddButton.vue";
import Todo from "./Todo.vue";

const isHidden = ref(true);

function slideIn() {
  setTimeout(() => isHidden.value = false, 1);
}

let lastId = 0;
const todos = ref([]);

function addTodo() {
  todos.value.push({
    "id": lastId + 1,
    "name": "",
    "done": false
  });
  lastId++;
}

onMounted(slideIn);
</script>

<template>
  <div class="panel" :class="{ hidden: isHidden }">
    <div class="controls-wrapper">
      <TodoFilter />
      <TodoAddButton @click="addTodo"/>
    </div>
    <div class="todos-wrapper">
      <TransitionGroup name="todo-list">
        <Todo v-for="todo in todos" :key="todo.id"
        :name="todo.name" :done="todo.done"
        @click-checkbox="todo.done = !todo.done"
        @update-name="value => todo.name = value"
        @delete="todos = todos.filter(i => i.id !== todo.id)" />
      </TransitionGroup>
    </div>
  </div>
</template>

<style scoped>
.todo-list-move,
.todo-list-enter-active, .todo-list-leave-active {
  transition: all .5s;
}

.todo-list-leave-active {
  position: absolute;
}

.todo-list-enter-from,
.todo-list-leave-to {
  opacity: 0;
}

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
  height: 100%;
  position: relative;
  overflow: scroll;
}

.todos-wrapper::-webkit-scrollbar {
  display: none;
}
</style>