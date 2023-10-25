function rendertasktemplate(task) {
    return `
        <li data-task-id="${task.id}" class="${task.completed ? "completed" : ""}> 
            <button data-action="completed"> </button>
            id: ${task.id}, title: ${task.title}
            <button data-action="update"> Edit </button>
            <button data-action="delete"> Delete </button>
            <button data-action="completed"> ${task.completed ? "✅" : "☑️"} </button>
        </li>`
} 
      