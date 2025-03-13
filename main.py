import os
import time
from operations import *
from models import Task

def main():
    tasks = []
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        option = input("Choose an option: ")

        # Crud
        if option == '1':
            pass
        
        # cRud
        if option == '2':
            read_task(tasks)
            
        # crUd
        if option == '3': 
            if not tasks:
                print("You don't have tasks yet!")
            else:
                read_task(tasks)
                ind = int(input("Which the position of the task you want to update? "))
                if ind >= 0 and ind < len(tasks):
                    new_name = input("What's your new task? ")
                    new_desc = input("What's your new description? ")
                    update_task(tasks, ind, new_name, new_desc)
                    print('Your task has been updated!')
                else: 
                    print(f"Choose a number between 0 and {len(tasks) - 1}")

        # cruD
        if option == '4':
            if not tasks:
                print("You don't have tasks yet!")
            else:
                read_task(tasks)
                num_task = int(input("Which the position of the task you want to delete? "))
                if num_task >= 0 and num_task < len(tasks):
                    delete_task(tasks, num_task)
                    print('Your task has been deleted!')
                else: 
                    print(f"Choose a number between 0 and {len(tasks) - 1}")
            
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
        print(".", end="", flush=True) 
        time.sleep(1)
    print()

if __name__ == "__main__":
    main()