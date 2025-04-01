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
        return False
    todo_list.append({"task": task, "priority": priority})
    save_todo_list(todo_list)
    return True

def edit_task(todo_list, task_number, new_task, new_priority):
    """Edit an existing task."""
    if 0 <= task_number < len(todo_list) and new_priority in PRIORITY_ORDER:
        todo_list[task_number] = {"task": new_task, "priority": new_priority}
        save_todo_list(todo_list)
        return True
    return False

def remove_task(todo_list, task_number):
    """Remove a task from the to-do list."""
    if 0 <= task_number < len(todo_list):
        todo_list.pop(task_number)
        save_todo_list(todo_list)
        return True
    return False

def reorder_task(todo_list, old_position, new_position):
    """Move a task to a new position in the list."""
    if 0 <= old_position < len(todo_list) and 0 <= new_position < len(todo_list):
        task = todo_list.pop(old_position)
        todo_list.insert(new_position, task)
        save_todo_list(todo_list)
        return True
    return False

def sort_by_priority(todo_list):
    """Sort tasks by priority."""
    todo_list.sort(key=lambda task: PRIORITY_ORDER[task["priority"]])
    save_todo_list(todo_list)
