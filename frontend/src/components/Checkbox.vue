<script setup>
defineProps(["done"]);
</script>

<template>
  <div class="checkbox">
    <svg :class="{ done }" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 512 512"><!-- Icon from All by undefined - undefined --><path d="M448 71.9c-17.3-13.4-41.5-9.3-54.1 9.1L214 344.2l-99.1-107.3c-14.6-16.6-39.1-17.4-54.7-1.8-15.6 15.5-16.4 41.6-1.7 58.1 0 0 120.4 133.6 137.7 147 17.3 13.4 41.5 9.3 54.1-9.1l206.3-301.7c12.6-18.5 8.7-44.2-8.6-57.5z" fill="currentColor"/></svg>
  </div>
</template>

<style scoped>
.checkbox {
  background-color: #2b2b2b;

  width: 2rem;
  height: 2rem;

  display: flex;
  justify-content: center;
  align-items: center;

  border: .125rem solid #4b4b4b;
  border-radius: .5rem;

  cursor: pointer;
}

svg {
  width: 1.25rem;

  opacity: 0;

  transition: opacity .125s;
}

svg.done {
  opacity: 1;
}
</style>