<script setup>
import { ref, useTemplateRef } from "vue";
import { onClickOutside } from "@vueuse/core";

const isActive = ref(false);

const box = useTemplateRef("box");

onClickOutside(box, () => isActive.value = false);
</script>

<template>
  <div class="wrapper">
    <div ref="box" class="box" @click="isActive = !isActive">
      <p>Невыполненные</p>
      <svg :class="{ active: isActive }" xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24"><path fill="currentColor" d="M8.12 9.29L12 13.17l3.88-3.88a.996.996 0 1 1 1.41 1.41l-4.59 4.59a.996.996 0 0 1-1.41 0L6.7 10.7a.996.996 0 0 1 0-1.41c.39-.38 1.03-.39 1.42 0"/></svg>
    </div>
    <Transition name="slide-fade">
      <div v-if="isActive" class="dropdown"></div>
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
  height: 300%;

  border: .125rem solid #4b4b4b;
  border-radius: 1rem;

  margin-top: .75rem;
}
</style>