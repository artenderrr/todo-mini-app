import { ref } from "vue";
import { createGlobalState } from "@vueuse/core";

export const useGlobalState = createGlobalState(() => {
    const initData = ref(null);
    const todos = ref(null);

    return { initData, todos };
});