import json

TODO_FILE = 'todos.json'
PRIORITY_ORDER = {"top": 1, "urgent": 2, "high": 3, "medium": 4, "low": 5, "background": 6, "deferred": 7}

def load_todos(filepath=TODO_FILE):
    """
    Read a text file and return the list of to-do items.
    :param filepath: text file where to-do list is stored
    :return: to-do list
    """
    with open(filepath, "r") as file:
        todos = json.load(file)
        return todos

def save_todos(todos, filepath=TODO_FILE):
    """
    Save (write) the to-do items list to the text file
    :param todos: to-do items in list
    :param filepath: text file where to-do list is stored
    :return: None
    """
    try:
        with open(filepath, "w") as file:
            json.dump(todos,file,indent=2)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def add_todo(todos,new_todo):
    """
    Add (append) to-do to to-do items list
    :param new_todo: to-do item to add
    :return: to-do items list
    """
    todos.append({'todo': new_todo})
    save_todos(todos)
    return todos

def update_todo(todos, index, new_todo):
    """ Update to-do list with the new to-do at the index in
    the to-do item list """
    # print(f"Replacing: {todos[number]}", end="")
    todos[index] = {'todo': new_todo}
    save_todos(todos)
    return todos


def drop_todo(todos, index):
    """ Drop to_do at the index in the to-do item list """
    del todos[index]
    save_todos(todos)
    return todos


if __name__ == "__main__":
    print("Hello from backend.py")
    print(load_todos())