<script setup>
import { ref, useTemplateRef } from "vue";
import { onClickOutside } from "@vueuse/core";

const emit = defineEmits(["filter-change"]);

const isActive = ref(false);

const box = useTemplateRef("box");

onClickOutside(box, () => isActive.value = false);

const options = ref(["Все", "Выполненные", "Невыполненные"]);

const chosenOption = ref(options.value[0]);

function changeFilter(option) {
  chosenOption.value = option;
  emit("filter-change", chosenOption.value);
  setTimeout(() => document.activeElement.blur(), 0);
}

defineExpose({ chosenOption });
</script>

<template>
  <div class="wrapper">
    <div ref="box" class="box" @click="isActive = !isActive">
      <p>{{ chosenOption }}</p>
      <svg :class="{ active: isActive }" xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24"><path fill="currentColor" d="M8.12 9.29L12 13.17l3.88-3.88a.996.996 0 1 1 1.41 1.41l-4.59 4.59a.996.996 0 0 1-1.41 0L6.7 10.7a.996.996 0 0 1 0-1.41c.39-.38 1.03-.39 1.42 0"/></svg>
    </div>
    <Transition name="slide-fade">
      <div v-if="isActive" class="dropdown">
        <div v-for="option in options" class="option" @click="changeFilter(option)">
          <p>{{ option }}</p>
          <svg v-if="option === chosenOption" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 12 12"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M9.765 3.205a.75.75 0 0 1 .03 1.06l-4.25 4.5a.75.75 0 0 1-1.075.015L2.22 6.53a.75.75 0 0 1 1.06-1.06l1.705 1.704l3.72-3.939a.75.75 0 0 1 1.06-.03"/></svg>
        </div>
      </div>
    </Transition>
  </div>
</template>

<style scoped>
.slide-fade-enter-active, .slide-fade-leave-active {
  transition: opacity .25s, transform .25s;
}

.slide-fade-enter-from, .slide-fade-leave-to {
  opacity: 0;
  transform: translateY(-4%);
}

.wrapper {
  width: 72.5%;
  height: 100%;
}

.box {
  background-color: #3b3b3b;

  font-size: 1.3rem;

  display: flex;
  justify-content: space-between;
  align-items: center;

  height: 100%;

  padding: 1rem;
  padding-right: .5rem;

  border: .125rem solid #4b4b4b;
  border-radius: 1rem;

  cursor: pointer;

  transition: filter .5s;
}

.box:hover {
  filter: brightness(1.1);
}

svg {
  width: 3.25rem;

  transition: transform .25s;
}

svg.active {
  transform: rotate(180deg);
}

.dropdown {
  position: relative;
  z-index: 1;

  background-color: #3b3b3b;

  width: 100%;

  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: .5rem;

  border: .125rem solid #4b4b4b;
  border-radius: 1rem;

  padding: .5rem;
  margin-top: .75rem;
}

.option {
  font-size: 1.3rem;

  height: 3.125rem;

  display: flex;
  justify-content: space-between;
  align-items: center;

  padding: .5rem;

  border-radius: .5rem;

  transition: background-color .25s;

  cursor: pointer;
}

.option:hover {
  background-color: #4b4b4b;
}
</style>