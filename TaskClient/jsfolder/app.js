fetchtasks();

const addtaskform = document.getElementById('add-task-form');
const addtaskbutton = document.getElementById('addtask');
const updatetaskbutton = document.getElementById('update-task');
addtaskform.addEventListener('submit', async (e) => {
    e.preventDefault();    
});

addtaskbutton.addEventListener('click', async function(e) {
    const formdata = new FormData(addtaskform);
    const task = {
        title: formdata.get('title'), 
        description: formdata.get('description')
    }
    await createtask(task);       
    fetchtasks();
});

updatetaskbutton.addEventListener('click', async function(e) {
    const formdata = new FormData(addtaskform);
    const task = {
        title: formdata.get('title'), 
        description: formdata.get('description')
    }
    const task_id = formdata.get('update-id');
    await updatetask(task_id, task);
    fetchtasks();
    addtaskform.classList.remove('editing-task');


});


const tasklist = document.getElementById('tasklist');
tasklist.addEventListener('click', async (e) => {
    if (e.target.nodeName === "BUTTON") {
            const action = e.target.getAttribute('data-action');
        if (action === "completed") {
            const li = e.target.parentNode;
            const task_id = li.getAttribute("data-task-id");
            const task = await fetchtask(task_id);
            await updatetask(task_id, {...task, completed: !task.completed});
            fetchtasks();


        }
        if (action === "delete") {
            const li = e.target.parentNode;
            const task_id = li.getAttribute("data-task-id");
            await deletetask(task_id);
            fetchtasks();
        }
        if (action === "update") {
            const li = e.target.parentNode;
            const task_id = li.getAttribute("data-task-id");
            const task = await fetchtask(task_id);
            const taskidinputelement = document.getElementById('task-id')
            const titleinputelement = document.getElementById('task-title');
            const descriptioneinputelement = document.getElementById('task-description');
            taskidinputelement.value = task.id;
            titleinputelement.value = task.title;
            descriptioneinputelement.value = task.description;
            addtaskform.classList.add('editing-task');


        }
    }
});

