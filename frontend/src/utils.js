export async function fetchTodos(initData) {
    const response = await fetch("https://artender.tech/api/tasks", {
        headers: {
            "Authorization": `tma ${initData}`
        }
    });

    if (!response.ok) {
        throw new Error(`Todos fetching failed with code ${response.status}`);
    }

    const todos = await response.json();

    return todos;
}