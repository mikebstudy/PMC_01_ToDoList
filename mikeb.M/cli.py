import backend as be
import time

def show_todos(todos):
    for index, todo in enumerate(todos):
        print(f"{index + 1}: {todo.strip("\n")}")



now = time.strftime("%b %d %Y %H:%M:%S")
print ("It is", now)

while True:
    user_action = input("Type add, show, edit, done, clear or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        new_todo = user_action[4:].strip()
        if new_todo == "":
            print("Nothing added")
            continue
        be.add_todo(new_todo)

    elif user_action == "show":
        todos = be.load_todos()
        show_todos(todos)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            # print(number)
            number -= 1
            todos = be.load_todos()
            if number < 0 or number >= len(todos):
                raise IndexError()
            print(f"Replacing: {todos[number]}", end="")
            edited_todo = input("Enter new todo: ")
            todos = be.update_todo(number, edited_todo)

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
            todos = be.load_todos()
            if number < 0 or number >= len(todos):
                raise IndexError()
            todos = be.drop_todo(number)

        except ValueError:
            # print(ValueError.args)
            print("Invalid input")

        except IndexError as error:
            # print(IndexError.args)
            # print(error)
            print("Number not in todo list")

    elif user_action.startswith("clear"):
        be.save_todos("")

    elif user_action == "exit":
        break

    else:
        print("Invalid command")