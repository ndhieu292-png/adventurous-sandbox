tasks = []
def add_task(task):
    tasks.append(task)
def remove_task(index):
    tasks.pop(index - 1)
def show_task():
    for index, task in enumerate(tasks):
        print(index + 1, task)
menu = ["1. Add task", "2. Show task", "3. Remove task", "4. Exit"]
while True:
    for choice in menu:
        print(choice)
    choice = input("Enter choice: ")
    if choice == "1":
        while True:
            task = input("Add task, q for quit: ")
            if task == "q":
                break
            add_task(task)
    elif choice == "2":
        show_task()
    elif choice == "3":
        while True:
            show_task()
            index = int(input("Remove task, 0 for quit: "))
            if index == 0:
                break
            elif len(tasks) == 0:
                print("Empty tasks")
            elif 0 < index <= len(tasks):
                remove_task(index)
            else:
                print("Invalid")
    elif choice == "4":
        break
