<script setup>
import { inject, onMounted, useTemplateRef } from "vue";
import Checkbox from "./Checkbox.vue";
import TodoInput from "./TodoInput.vue";

defineProps(["name", "done"]);

const card = useTemplateRef("card");

function scrollIntoView() {
  const slideInFinished = inject("slideInFinished");
  if (slideInFinished.value) {
    setTimeout(() => {
      card.value.scrollIntoView({ behavior: "smooth", block: "end" });
    }, 0);
  }
}

onMounted(scrollIntoView);
</script>

<template>
  <div class="card" ref="card">
    <Checkbox v-bind="{ done }" @click="$emit('click-checkbox')" />
    <TodoInput v-bind="{ name, done }"
    @left-empty="$emit('delete')"
    @update-name="value => $emit('update-name', value)" />
    <svg class="trash" @click="$emit('delete')" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M7 21q-.825 0-1.412-.587T5 19V6q-.425 0-.712-.288T4 5t.288-.712T5 4h4q0-.425.288-.712T10 3h4q.425 0 .713.288T15 4h4q.425 0 .713.288T20 5t-.288.713T19 6v13q0 .825-.587 1.413T17 21zm5-7.1l1.9 1.9q.275.275.7.275t.7-.275t.275-.7t-.275-.7l-1.9-1.9l1.9-1.9q.275-.275.275-.7t-.275-.7t-.7-.275t-.7.275L12 11.1l-1.9-1.9q-.275-.275-.7-.275t-.7.275t-.275.7t.275.7l1.9 1.9l-1.9 1.9q-.275.275-.275.7t.275.7t.7.275t.7-.275z"/></svg>
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
  margin-bottom: 1rem;

  border: .125rem solid #4b4b4b;
  border-radius: 1rem;
}

.trash {
  cursor: pointer;

  transition: transform .25s;
}

.trash:active {
  transform: scale(.75);
}
</style>