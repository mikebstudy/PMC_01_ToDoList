import json

TODO_FILE = "todo_list.json"
PRIORITY_ORDER = {"high": 1, "medium": 2, "low": 3}


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


def add_task(todo_list, task, priority):
    """Add a new task with priority."""
    if priority not in PRIORITY_ORDER:
        print("Invalid priority! Choose from high, medium, or low.")
        return
    todo_list.append({"task": task, "priority": priority})
    save_todo_list(todo_list)


def edit_task(todo_list, task_number, new_task, new_priority):
    """Edit an existing task."""
    if 0 <= task_number < len(todo_list):
        if new_priority not in PRIORITY_ORDER:
            print("Invalid priority! Choose from high, medium, or low.")
            return
        todo_list[task_number] = {"task": new_task, "priority": new_priority}
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


def reorder_task(todo_list, old_position, new_position):
    """Move a task to a new position in the list."""
    if 0 <= old_position < len(todo_list) and 0 <= new_position < len(todo_list):
        task = todo_list.pop(old_position)
        todo_list.insert(new_position, task)
        save_todo_list(todo_list)
    else:
        print("Invalid positions.")


def sort_by_priority(todo_list):
    """Sort tasks by priority."""
    todo_list.sort(key=lambda task: PRIORITY_ORDER[task["priority"]])
    save_todo_list(todo_list)


def display_todo_list(todo_list):
    """Display the to-do list with priorities."""
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(todo_list):
            print(f"{i + 1}. [{task['priority'].capitalize()}] {task['task']}")


def main():
    todo_list = load_todo_list()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Remove Task")
        print("5. Reorder Task")
        print("6. Sort by Priority")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            task = input("Enter the task: ").strip()
            priority = input("Enter priority (high, medium, low): ").strip().lower()
            add_task(todo_list, task, priority)
        elif choice == "3":
            display_todo_list(todo_list)
            task_number = int(input("Enter task number to edit: ")) - 1
            new_task = input("Enter the new task: ").strip()
            new_priority = input("Enter new priority (high, medium, low): ").strip().lower()
            edit_task(todo_list, task_number, new_task, new_priority)
        elif choice == "4":
            display_todo_list(todo_list)
            task_number = int(input("Enter task number to remove: ")) - 1
            remove_task(todo_list, task_number)
        elif choice == "5":
            display_todo_list(todo_list)
            old_position = int(input("Enter the current task number: ")) - 1
            new_position = int(input("Enter the new position: ")) - 1
            reorder_task(todo_list, old_position, new_position)
        elif choice == "6":
            sort_by_priority(todo_list)
            print("Tasks sorted by priority.")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
