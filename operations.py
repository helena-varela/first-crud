from task import Task

def create_task(tasks, add_name, add_desc):
    tarefa = Task(name = add_name,description = add_desc)
    tasks.append(tarefa)

def read_task(tasks):
    if not tasks:
        print("You don't have tasks yet!")
    else: 
        tar = 0
        for t in tasks:
            print(f"{str(tar)}. {str(t)}")
            tar += 1

def update_task(tasks, ind, new_name, new_desc):
    old_task = tasks[ind]
    old_task.name = new_name
    old_task.description = new_desc

def delete_task(tasks, num_task):
    tasks.pop(num_task)