TODO_FILE = 'todos.txt'

def load_todos(filepath=TODO_FILE):
    """
    Read a text file and return the list of to-do items.
    :param filepath: text file where to-do list is stored
    :return: to-do list
    """
    with open(filepath, "r") as file:
        todos = file.readlines()
        return todos

def save_todos(todos, filepath=TODO_FILE):
    """
    Save (write) the to-do items list to the text file
    :param todos: to-do items in list
    :param filepath: text file where to-do list is stored
    :return: None
    """
    with open(filepath, "w") as file:
        file.writelines(todos)

def add_todo(new_todo):
    """
    Add (append) to-do to to-do items list
    :param new_todo: to-do item to add
    :return: to-do items list
    """
    todos = load_todos()
    todos.append(new_todo + "\n")
    save_todos(todos)
    return todos

def update_todo(index, new_todo):
    """
    Update to-do list with the new to-do at the index in
    the to-do item list
    :param index: index of location to update in the to-do item list
    :param new_todo: to-do to put into the to-do item list
    :return: updated to-do item list
    """
    todos = load_todos()
    # print(f"Replacing: {todos[number]}", end="")
    todos[index] = new_todo + "\n"
    save_todos(todos)
    return todos

def drop_todo(index):
    """
    Drop to_do at the index in the to-do item list
    :param index: index into the to-do list
    :return: to-do item list
    """
    todos = load_todos()
    del todos[index]
    save_todos(todos)
    return todos


if __name__ == "__main__":
    print("Hello from backend.py")
    print(load_todos())