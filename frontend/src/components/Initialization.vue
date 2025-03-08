<script setup>
import { ref, onMounted } from "vue";

const emit = defineEmits(["complete"]);
const initState = ref("pending");

function parseInitData() {
  return window.location.hash.slice(14).split("&")[0];
}

async function validateInitData(initData) {
  const response = await fetch("http://localhost:8000/api/tasks", {
    headers: {
      "Authorization": `tma ${initData}`
    }
  });
  return response.ok;
}

async function initialize() {
  const initData = parseInitData();
  const validInitData = await validateInitData(initData);
  initState.value = validInitData ? "success" : "failure";
  emit("complete", initState.value);
}

onMounted(initialize);
</script>

<template>
  <p>Initialization</p>
</template>