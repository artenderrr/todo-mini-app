export async function fetchTodos(initData) {
    const response = await fetch("http://localhost:8000/api/tasks", {
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