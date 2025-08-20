# Simple To-Do List Application

tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "✅" if task["done"] else "❌"
            print(f"{i+1}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    print("Task added successfully!")

def update_task():
    view_tasks()
    index = int(input("Enter task number to update: ")) - 1
    if 0 <= index < len(tasks):
        new_title = input("Enter new title: ")
        tasks[index]["title"] = new_title
        print("Task updated!")
    else:
        print("Invalid task number.")

def mark_done():
    view_tasks()
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted!")
    else:
        print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
