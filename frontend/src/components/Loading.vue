<template>
  <svg viewBox="0 0 50 50">
    <circle 
    cx="25" cy="25" fill="none" r="21"
    stroke-width="7.5" stroke="#cdcdcd"
    stroke-dasharray="95 50"
    stroke-linecap="round" />
  </svg>
</template>

<style scoped>
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

svg {
  width: 3.5rem;
  animation: spin 1s linear infinite;
}
</style>