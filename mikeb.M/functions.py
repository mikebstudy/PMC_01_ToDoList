TODO_FILE = 'todos.txt'

def get_todos(filepath=TODO_FILE):
    """
    Read a text file and return the list
    of to-do items.
    :param filepath: text file where to-do list is stored
    :return: to-do list
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
        return todos_local

def save_todos(todos_arg, filepath=TODO_FILE):
    """
    Save (write) the to-do items list to the text file
    :param todos_arg: to-do items in list
    :param filepath:
    :return:
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())