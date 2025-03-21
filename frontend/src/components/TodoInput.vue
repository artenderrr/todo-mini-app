<script setup>
import { ref, inject, onMounted, useTemplateRef } from "vue";

const emit = defineEmits(["update-name", "left-empty"]);

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

function handleBlur(e) {
  const content = e.target.innerText;
  if (content.length === 0 || content === "\n") {
    emit("left-empty");
  } else {
    emit("update-name", content);
  }
}

const inputField = useTemplateRef("inputField");

function blurOnEnter() {
  inputField.value.blur();
  window.getSelection()?.removeAllRanges();
}

function focus() {
  const slideInFinished = inject("slideInFinished");
  if (slideInFinished.value) {
    inputField.value.focus();
  }
}

onMounted(focus);
</script>

<template>
  <div class="wrapper" :class="{ warning }">
    <p ref="inputField" :class="{ done }"
    contenteditable
    @keydown.enter="blurOnEnter"
    @blur="handleBlur"
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