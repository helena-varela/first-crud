from task import Task

def create_task(tasks, add_name, add_desc):
    tarefa = Task(name = add_name,description = add_desc)
    tasks.append(tarefa)

def read_task(tasks):
    if not tasks:
        print("You don't have tasks yet!")
    else: 
        for t in tasks:
            print(t) 

def update_task(tasks, ind, new_name, new_desc):
    old_task = tasks[ind]
    old_task.name = new_name
    old_task.description = new_desc

def delet_task(tasks, num_task):
    if num_task >= 0 and num_task < len(tasks):
        tasks.pop(num_task)
    else: print(f"Choose a number between 0 and {len(tasks) - 1}") 