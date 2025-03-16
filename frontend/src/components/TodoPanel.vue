<script setup>
import { ref, computed, provide, onMounted, useTemplateRef } from "vue";
import TodoFilter from "./TodoFilter.vue";
import TodoAddButton from "./TodoAddButton.vue";
import Todo from "./Todo.vue";

const isHidden = ref(true);

const slideInFinished = ref(false);
provide("slideInFinished", slideInFinished);

function slideIn() {
  document.activeElement.blur();
  setTimeout(() => {
    isHidden.value = false;
    setTimeout(() => slideInFinished.value = true, 1000);
  }, 1);
}

let lastId = 1;
const todos = ref([
  { id: 1, name: "Wake up", done: false }
]);
const todoFilter = ref("Все");

const filteredTodos = computed(() => {
  return todoFilter.value === "Все" ? todos.value : todos.value.filter(todo => {
    return todoFilter.value === "Выполненные" ? todo.done : !todo.done;
  });
});

const todoFilterElement = useTemplateRef("todoFilter");

function addTodo() {
  todoFilter.value = "Все";
  todoFilterElement.value.chosenOption = todoFilter.value;
  setTimeout(() => {
    todos.value.push({
      "id": lastId + 1,
      "name": "",
      "done": false
    });
    lastId++;
  }, 1);
}

onMounted(slideIn);
</script>

<template>
  <div class="panel" :class="{ hidden: isHidden }">
    <div class="controls-wrapper">
      <TodoFilter ref="todoFilter" @filter-change="value => todoFilter = value" />
      <TodoAddButton @click="addTodo"/>
    </div>
    <div class="todos-wrapper">
      <Transition name="fade" mode="out-in">
        <div v-if="filteredTodos.length === 0" class="placeholder">
          <p>Задач пока нет</p>
        </div>
        <TransitionGroup v-else name="todo-list" tag="div">
          <Todo v-for="todo in filteredTodos" :key="todo.id"
          :name="todo.name" :done="todo.done"
          @click-checkbox="todo.done = !todo.done"
          @update-name="value => todo.name = value"
          @delete="todos = todos.filter(i => i.id !== todo.id)" />
        </TransitionGroup>
      </Transition>
    </div>
  </div>
</template>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity .25s;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

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
  height: 4rem;

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

.placeholder {
  color: #5b5b5b;

  width: 100%;
  height: 100%;

  display: flex;
  justify-content: center;
}

.placeholder > p {
  margin-top: .5rem;
}
</style>