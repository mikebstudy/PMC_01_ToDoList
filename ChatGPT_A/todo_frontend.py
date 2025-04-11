import todo_backend as backend


def display_todo_list(todo_list):
    """Display the to-do list with priorities."""
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(todo_list):
            print(f"{i + 1}. [{task['priority'].capitalize()}] {task['task']}")


def main():
    todo_list = backend.load_todo_list()

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
            if backend.add_task(todo_list, task, priority):
                print("Task added successfully!")
            else:
                print("Invalid priority. Please use high, medium, or low.")
        elif choice == "3":
            display_todo_list(todo_list)
            try:
                task_number = int(input("Enter task number to edit: ")) - 1
                new_task = input("Enter the new task: ").strip()
                new_priority = input("Enter new priority (high, medium, low): ").strip().lower()
                if backend.edit_task(todo_list, task_number, new_task, new_priority):
                    print("Task edited successfully!")
                else:
                    print("Invalid input. Please check the task number and priority.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            display_todo_list(todo_list)
            try:
                task_number = int(input("Enter task number to remove: ")) - 1
                if backend.remove_task(todo_list, task_number):
                    print("Task removed successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            display_todo_list(todo_list)
            try:
                old_position = int(input("Enter the current task number: ")) - 1
                new_position = int(input("Enter the new position: ")) - 1
                if backend.reorder_task(todo_list, old_position, new_position):
                    print("Task reordered successfully!")
                else:
                    print("Invalid positions.")
            except ValueError:
                print("Please enter valid numbers.")
        elif choice == "6":
            backend.sort_by_priority(todo_list)
            print("Tasks sorted by priority.")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()