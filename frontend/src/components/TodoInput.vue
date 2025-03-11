<script setup>
import { ref } from "vue";

const warning = ref(false);

function highlightBorders() {
  warning.value = true;
  setTimeout(() => warning.value = false, 1000);
}

let previousContent = "";

function restrictLength(e) {
  const newContent = e.target.innerText;
  if (newContent.length > 64) {
    highlightBorders();
    e.target.innerText = previousContent;
    e.target.blur();
  } else {
    previousContent = newContent;
  }
}
</script>

<template>
  <div class="wrapper" :class="{ warning }">
    <p
    contenteditable
    @keydown.enter="e => e.target.blur()"
    @input="restrictLength"></p>
  </div>
</template>

<style scoped>
.wrapper {
  --error-brdr-clr: #b51e46;
}

.wrapper {
  width: 67.5%;

  padding: .125rem;
  
  border-radius: .5rem;

  transition: background-color .5s;
}

.wrapper.warning {
  background-color: var(--error-brdr-clr);
}

p {
  background-color: #3b3b3b;

  font-size: 1.3rem;
  
  padding: .5rem;
  
  border-radius: calc(.5rem - .125rem);
  outline: none;
}
</style>