import os
import time

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
            pass
        if option == '2':
            pass
        if option == '3':
            pass
        if option == '4':
            pass
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
