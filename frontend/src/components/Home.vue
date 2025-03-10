<script setup>
import AppHeader from "./AppHeader.vue";
import TodoPanel from "./TodoPanel.vue";
</script>

<template>
  <div class="wrapper">
    <div class="app-header-wrapper">
      <AppHeader />
    </div>
    <TodoPanel />
  </div>
</template>

<style scoped>
.wrapper {
  height: 100%;
  width: 100%;
}

.app-header-wrapper {
  height: 20%;

  display: flex;
  justify-content: center;
  align-items: center;
}
</style>