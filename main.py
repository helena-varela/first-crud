import json
import os
import time
from operations import * 


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
            create_tasks(tasks) 
        
        # cRud
        if option == '2':
            read_tasks(tasks)
            
        # crUd
        if option == '3':
            update_tasks(tasks)
            
        # cruD
        if option == '4':
            delete_tasks(tasks)

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