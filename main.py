import os
import time

from task import Task

def main():
    tasks = []
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Remove Task")
        print("5. Exit")
        option = input("Choose an option: ")

        if option == '1':
            add_name = input("What's your task:\n")
            add_desc = input('Describe your task:\n')
            tarefa = Task(name = add_name,description = add_desc)
            tasks.append(tarefa)
            print('Your task has been added!')

        if option == '2':
            for t in tasks:
                print(t)

        if option == '3':
            pass

        if option == '4':
            num_task = int(input("What's the position of the task you wanna delete? "))
            if num_task >= 0 and num_task < len(tasks):
                tasks.pop(num_task)
            else: print(f"Choose a number between 0 and {len(tasks) }")
            
        if option == '5':
            print("Exiting")
            break

        loading()
        clear_console()

def clear_console():
    os.system('clear')

def loading():
    print("Loading", end="")
    for _ in range(3):
        print(".", end="", flush=True)  # flush ensures the dot is printed immediately
        time.sleep(1)
    print()  # new line

if __name__ == "__main__":
    main()