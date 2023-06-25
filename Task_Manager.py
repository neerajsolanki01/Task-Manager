tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    if len(tasks) == 0:
        print("No tasks to remove.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
        task_number = int(input("Enter the task number to remove: "))
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number!")
        else:
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

def task_manager():
    print("Welcome to the Task Manager!")

    while True:
        print("\nSelect an option:")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. View Tasks")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            print("Thank you for using the Task Manager. Goodbye!")
            break

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice < 1 or choice > 3:
            print("Invalid choice! Please select a valid option.")
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            view_tasks()

task_manager()
