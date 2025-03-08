<script setup>
import { ref } from "vue";
import Initialization from "./components/Initialization.vue";
import Home from "./components/Home.vue";

const initState = ref("pending");
</script>

<template>
  <Transition name="fade" mode="out-in">
    <Initialization v-if="initState !== 'success'" @complete="result => initState = result" />
    <Home v-else/>
  </Transition>
</template>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>