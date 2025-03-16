<script setup>
import { ref, onMounted } from "vue";
import { useGlobalState } from "../store.js";
import { fetchTodos } from "../utils.js";
import AppHeader from "./AppHeader.vue";
import Loading from "./Loading.vue";
import InitError from "./InitError.vue";

const emit = defineEmits(["complete"]);
const initState = ref("pending");

const { initData, todos } = useGlobalState();

function parseInitData() {
  return window.location.hash.slice(14).split("&")[0];
}

async function initialize() {
  try {
    initData.value = parseInitData();
    todos.value = await fetchTodos(initData.value);
    initState.value = "success";
  } catch (error) {
    console.error(error);
    initState.value = "failure";
  } emit("complete", initState.value);
}

onMounted(initialize);
</script>

<template>
  <div class="wrapper">
    <AppHeader />
    <Transition name="fade" mode="out-in">
      <Loading v-if="initState === 'pending'" />
      <InitError v-else-if="initState === 'failure'" />
    </Transition>
  </div>
</template>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}
</style>