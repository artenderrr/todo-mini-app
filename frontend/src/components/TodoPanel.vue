<script setup>
import { ref, onMounted } from "vue";

const isHidden = ref(true);

function slideIn() {
  setTimeout(() => isHidden.value = false, 1);
}

onMounted(slideIn);
</script>

<template>
  <div class="panel" :class="{ hidden: isHidden }"></div>
</template>

<style scoped>
.panel {
  background-color: #2b2b2b;

  width: 40rem;
  max-width: 100%;
  height: 100%;

  border: .125rem solid #3b3b3b;
  border-bottom: none;
  border-top-left-radius: 2rem;
  border-top-right-radius: 2rem;

  margin: auto;

  transition: transform 1s;
}

.panel.hidden {
  transform: translateY(100%);
}
</style>