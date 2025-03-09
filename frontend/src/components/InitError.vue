<template>
  <div class="card">
    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 1024 1024"><!-- Icon from All by undefined - undefined --><path fill="currentColor" d="M512 64a448 448 0 1 1 0 896a448 448 0 0 1 0-896m0 192a58.43 58.43 0 0 0-58.24 63.744l23.36 256.384a35.072 35.072 0 0 0 69.76 0l23.296-256.384A58.43 58.43 0 0 0 512 256m0 512a51.2 51.2 0 1 0 0-102.4a51.2 51.2 0 0 0 0 102.4"/></svg>
    <p>Ошибка загрузки</p>
  </div>
</template>

<style scoped>
.card {
  --error-bg-clr: #b51e46;
  --error-brdr-clr: #e1446e;
  --error-fg-clr: #ff85a5;
}

.card {
  background-color: var(--error-bg-clr);
  color: var(--error-fg-clr);

  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;

  border: .125rem solid var(--error-brdr-clr);
  border-radius: 1rem;

  padding: 1rem;

  transition: transform .5s;
}

p {
  font-size: 1.5rem;
}
</style>