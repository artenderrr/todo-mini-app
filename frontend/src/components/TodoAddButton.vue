<script setup>
import { ref } from "vue";

const defaultIconWidth = 2;
const iconWidth = ref(defaultIconWidth);

function onMouseDown() {
  iconWidth.value /= 1.125;
}

function onMouseUp() {
  iconWidth.value = defaultIconWidth;
}
</script>

<template>
  <button @mousedown="onMouseDown" @mouseup="onMouseUp">
    <svg :style="{ width: iconWidth + 'rem' }" xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 512 512"><!-- Icon from All by undefined - undefined --><path d="M417.4 224H288V94.6c0-16.9-14.3-30.6-32-30.6s-32 13.7-32 30.6V224H94.6C77.7 224 64 238.3 64 256s13.7 32 30.6 32H224v129.4c0 16.9 14.3 30.6 32 30.6s32-13.7 32-30.6V288h129.4c16.9 0 30.6-14.3 30.6-32s-13.7-32-30.6-32z" fill="currentColor"/></svg>
  </button>
</template>

<style scoped>
button {
  background-color: #3b3b3b;
  color: #cdcdcd;

  width: 22.5%;
  height: 100%;

  display: flex;
  justify-content: center;
  align-items: center;

  border: .125rem solid #4b4b4b;
  border-radius: 1rem;

  cursor: pointer;

  transition: filter .5s, transform .125s;
}

button:hover {
  filter: brightness(1.1);
}

svg {
  transition: width .125s;
}
</style>