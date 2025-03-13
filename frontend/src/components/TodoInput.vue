<script setup>
import { ref, onMounted, useTemplateRef } from "vue";

const emit = defineEmits(["update-name"]);

defineProps(["name", "done"]);

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

function updateName(e) {
  emit("update-name", e.target.innerText);
}

const inputField = useTemplateRef("inputField");

function blurOnEnter() {
  inputField.value.blur();
  window.getSelection()?.removeAllRanges();
}

onMounted(() => inputField.value.focus());
</script>

<template>
  <div class="wrapper" :class="{ warning }">
    <p ref="inputField" :class="{ done }"
    contenteditable
    @keydown.enter="blurOnEnter"
    @blur="updateName"
    @input="restrictLength">{{ name }}</p>
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

  transition: color .125s;
}

p.done {
  color: #5b5b5b;
}
</style>