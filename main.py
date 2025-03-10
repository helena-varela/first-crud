import os
import time
from operations import *
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

        # Crud
        if option == '1':
            add_name = input("What's your task:\n")
            add_desc = input('Describe your task:\n')
            create_task(tasks, add_name, add_desc)
            print('Your task has been added!')
        
        # cRud
        if option == '2':
            read_task(tasks)
            
        # crUd
        if option == '3': 
            if not tasks:
                print("You don't have tasks yet!")
            else:
                read_task(tasks)
                ind = int(input("What's the position of the task you wanna update? "))
                new_name = input("What's your new task? ")
                new_desc = input("What's your new description? ")
                update_task(tasks, ind, new_name, new_desc)
                print('Your task has been updated!')

        # cruD
        if option == '4':
            if not tasks:
                print("You don't have tasks yet!")
            else:
                num_task = int(input("What's the position of the task you wanna delete? "))
                delet_task(tasks, num_task)
                print('Your task has been deleted!')
            
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