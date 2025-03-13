import json

def create_tasks(tasks):
    name_task = input("What's the name of your task? ")
    desc_task = input("What's the description of your task? ")
    dic = { "name": name_task,
            "description" : desc_task
            }
    try:
        with open("tasks.json","r") as file: # abre o tasks.json no modo leitura
            tasks = json.load(file) # armazena na variavel tasks o json
    except (FileNotFoundError, json.JSONDecodeError): # se o json nao existir ou for corrompido
        tasks = [] # tasks é inicializada como uma lista vazia
    
    tasks.append(dic) # adiciona dic à tasks
    print("Your task has been added!")
    with open("tasks.json","w") as file: # abre o arquivo no modo escrita 
        json.dump(tasks, file, indent = 4)


def read_tasks(tasks):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("You don't have tasks yet!")
    index = 0
    for t in tasks:
        print(f"{str(index)}. {t['name']}: {t['description']}")
        index += 1

def update_tasks(tasks):
    try:
        with open("tasks.json","r") as file:
            tasks = json.load(file)
        read_tasks(tasks)
    except (FileNotFoundError, json.JSONDecodeError):
        print("You don't have tasks yet!")
    else:
        try:
            ind = int(input("Which the position of the task you want to update? "))
            if ind >= 0 and ind < len(tasks):
                new_name = input("What's your new task? ")
                new_desc = input("What's your new description? ")
                old_task = tasks[ind]
                old_task["name"] = new_name
                old_task["description"] = new_desc
                with open("tasks.json","w") as file:
                    json.dump (tasks, file, indent=4)
                print('Your task has been updated!')
            else: 
                print(f"Choose a number between 0 and {len(tasks) - 1}")
        except ValueError:
            print("Enter a number, please")
        

def delete_tasks(tasks):
    try:
        with open("tasks.json","r") as file:
            tasks = json.load(file)
        read_tasks(tasks)
    except (FileNotFoundError, json.JSONDecodeError):
        print("You don't have tasks yet!")
    else:
        try:   
            num_task = int(input("Which the position of the task you want to delete? "))
            if num_task >= 0 and num_task < len(tasks):
                tasks.pop(num_task)
                with open("tasks.json","w") as file:
                    json.dump(tasks, file, indent=4)
                print('Your task has been deleted!')
            else: 
                print(f"Choose a number between 0 and {len(tasks) - 1}")
        except ValueError:
            print("Enter a number, please")