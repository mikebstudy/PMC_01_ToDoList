import json

TODO_FILE = "todo_list.json"


def load_todo_list():
    """Load the to-do list from a file."""
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_todo_list(todo_list):
    """Save the to-do list to a file."""
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file, indent=4)


def add_task(todo_list, task):
    """Add a new task to the to-do list."""
    todo_list.append(task)
    save_todo_list(todo_list)


def edit_task(todo_list, task_number, new_task):
    """Edit an existing task."""
    if 0 <= task_number < len(todo_list):
        todo_list[task_number] = new_task
        save_todo_list(todo_list)
    else:
        print("Invalid task number.")


def remove_task(todo_list, task_number):
    """Remove a task from the to-do list."""
    if 0 <= task_number < len(todo_list):
        todo_list.pop(task_number)
        save_todo_list(todo_list)
    else:
        print("Invalid task number.")


def display_todo_list(todo_list):
    """Display the to-do list."""
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(todo_list):
            print(f"{i + 1}. {task}")


def main():
    todo_list = load_todo_list()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            task = input("Enter the task: ").strip()
            add_task(todo_list, task)
        elif choice == "3":
            display_todo_list(todo_list)
            task_number = int(input("Enter task number to edit: ")) - 1
            new_task = input("Enter the new task: ").strip()
            edit_task(todo_list, task_number, new_task)
        elif choice == "4":
            display_todo_list(todo_list)
            task_number = int(input("Enter task number to remove: ")) - 1
            remove_task(todo_list, task_number)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
