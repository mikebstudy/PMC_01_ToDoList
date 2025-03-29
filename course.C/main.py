from functions import get_todos, save_todos
import time

now = time.strftime("%b %d %Y %H:%M:%S")
print ("It is", now)

while True:
    user_action = input("Type add, show, edit, done, clear or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()
        todos = get_todos()
        # print(todos)
        todos.append(todo + "\n")
        # print(todos)
        save_todos(todos)

    elif user_action == "show":
        todos = get_todos()
        for index, todo in enumerate(todos):
            print(f"{index + 1}: {todo.strip("\n")}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            # print(number)
            number -= 1
            todos = get_todos()
            print(f"Replacing: {todos[number]}", end="")
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            save_todos(todos)
        except ValueError:
            # print(ValueError.args)
            print("Invalid input")
        except IndexError:
            # print(IndexError.args)
            print("Number not in todo list")

    elif user_action.startswith("done"):
        try:
            number = int(user_action[5:])
            # print(number)
            number -= 1
            todos = get_todos()
            del todos[number]
            save_todos(todos)
        except ValueError:
            # print(ValueError.args)
            print("Invalid input")
        except IndexError:
            # print(IndexError.args)
            print("Number not in todo list")

    elif user_action == "exit":
        break

    elif user_action.startswith("clear"):
        save_todos("")

    else:
        print("Invalid command")