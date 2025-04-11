import backend as be
import time

AUTO_SHOW_TODOS = 7

def show_todos(todos):
    for index, todo in enumerate(todos):
        priority = todo['priority']
        priority_len = len(priority) - 3
        # space = "     "[priority_len+1:]
        space = " "
        print(f"{index + 1}: [{priority}]{space}{todo['todo']}")

def auto_show_todos(todos):
    if len(todos) < AUTO_SHOW_TODOS:
        show_todos(todos)

now = time.strftime("%b %d %Y %H:%M:%S")
print ("It is", now)

def main():
    todos = be.load_todos()

    while True:
        # user_action = input("Type \x1B[4ma\x1b[0mdd, show, edit, drop, done, clear or exit: ")
        user_action = input("Type add, show, edit, drop, done, clear or exit: ")
        user_action = user_action.strip()

        if user_action.startswith("add"):
            new_todo = user_action[4:].strip()
            if new_todo == "":
                print("Nothing added")
                continue
            priority = input("Enter priority (top, urgent, high, medium, low, background, deferred ): ").strip().lower()
            if priority in be.PRIORITY_ORDER:
                todos = be.add_todo(todos, new_todo, priority)
                auto_show_todos(todos)
            else:
                print("Invalid input. Please check priority.")


        elif user_action == "show":
            show_todos(todos)

        elif user_action.startswith("edit"):
            try:
                number = int(user_action[5:])
                # print(number)
                number -= 1
                if number < 0 or number >= len(todos):
                    raise IndexError()
                print(f"Old todo: {todos[number]["todo"]}")
                edited_todo = input("New todo: ")
                priority = input(
                    "Enter priority (top, urgent, high, medium, low, background, deferred ): ").strip().lower()
                if priority in be.PRIORITY_ORDER:
                    todos = be.update_todo(todos, number, edited_todo, priority)
                    auto_show_todos(todos)
                else:
                    print("Invalid input. Please check the task number and priority.")


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
                if number < 0 or number >= len(todos):
                    raise IndexError()
                todos = be.drop_todo(todos, number)
                auto_show_todos(todos)

            except ValueError:
                # print(ValueError.args)
                print("Invalid input")

            except IndexError as error:
                # print(IndexError.args)
                # print(error)
                print("Number not in todo list")

        elif user_action.startswith("drop"):
            try:
                number = int(user_action[5:])
                # print(number)
                number -= 1
                if number < 0 or number >= len(todos):
                    raise IndexError()
                todos = be.drop_todo(todos,number)
                auto_show_todos(todos)

            except ValueError:
                # print(ValueError.args)
                print("Invalid input")

            except IndexError as error:
                # print(IndexError.args)
                # print(error)
                print("Number not in todo list")

        elif user_action.startswith("clear"):
            be.save_todos([])
            auto_show_todos(todos)

        elif user_action == "exit":
            break

        else:
            print("Invalid command")

if __name__ == "__main__":
    main()