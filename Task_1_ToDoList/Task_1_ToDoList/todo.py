# Task 1: To-Do List Application
tasks = []
def display_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")
def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks):
            status = "Done" if task["done"] else "Pending"
            print(f"{index + 1}. {task['title']} - [{status}]")
def add_task():
    title = input("Enter task title: ")
    task = {"title": title, "done": False}
    tasks.append(task)
    print("Task added successfully.")
def mark_task_done():
    view_tasks()
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def delete_task():
    view_tasks()
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed_task = tasks.pop(choice - 1)
            print(f"Task '{removed_task['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
while True:
    display_menu()
    user_choice = input("Enter your choice (1-5): ")
    if user_choice == '1':
        view_tasks()
    elif user_choice == '2':
        add_task()
    elif user_choice == '3':
        mark_task_done()
    elif user_choice == '4':
        delete_task()
    elif user_choice == '5':
        print("Exiting To-Do List. Thank you!")
        break
    else:
        print("Invalid choice. Please select between 1 and 5.")
