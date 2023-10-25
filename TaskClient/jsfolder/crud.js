const Base_URL = "http://localhost:8000/tasks/";


async function createtask(task) {
    task.category = [0];
    task.user = 1;
    try {
        const response = await fetch(Base_URL, {
            method: 'POST', 
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${localStorage.getItem('token')}`
            },
            body: JSON.stringify(task)       
        });

        const json = await response.json();
        return json;
        
    }  catch (error) {
        throw new Error(error);
    } 
}

async function deletetask(task_id) {
    try {
        const response = await fetch(`${Base_URL}${task_id}`, {
            method: 'DELETE', 
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${localStorage.getItem('token')}`
            },       
        });
    }  catch (error) {
        throw new Error(error);
    }     
}
const taskslist = document.getElementById("tasklist");
async function fetchtasks() {
    const response = await fetch(Base_URL, {
        method: 'GET', 
        headers: {
            'Authorization': `Token ${localStorage.getItem('token')}`
        }
     
    });
    const data = await response.json();
    const tasks = data.results;
    let taskslistrenderstring = "";
        for (let task of tasks) {
            taskslistrenderstring = taskslistrenderstring + rendertasktemplate(task);
        }

        taskslist.innerHTML = taskslistrenderstring;
}

async function updatetask(task_id, task) {
    task.category = [0];
    task.user = 1;
    try {
        const response = await fetch(`${Base_URL}${task_id}/`, {
            method: 'PUT', 
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${localStorage.getItem('token')}`
                
            },
            body: JSON.stringify(task)       
        });

        const json = await response.json();
        return json;
        
    }  catch (error) {
        throw new Error(error);
    } 

}


async function fetchtask(task_id) {
    const response = await fetch(`${Base_URL}${task_id}/`, {
        headers: {
            'Authorization': `Token ${localStorage.getItem('token')}`
        }
    });
    return await response.json();

}