from functions import get_todos, save_todos, TODO_FILE
import FreeSimpleGUI as fsg
import time
import os

if not os.path.exists(TODO_FILE):
    with open(TODO_FILE, "w") as file:
        pass

fsg.theme("Black")

clock = fsg.Text('', key="clock")

label = fsg.Text("Type in a todo")
input_box = fsg.InputText(tooltip="Enter todo", key="todo")
add_button = fsg.Button("Add")
list_box = fsg.Listbox(values=get_todos(), key="todos",
                       enable_events=True, size=(45, 10))
edit_button = fsg.Button("Edit")
done_button = fsg.Button("Done")
exit_button = fsg.Button("Exit")


window = fsg.Window("ToDo List",
                    layout=[
                        [clock],
                        [label],
                        [input_box, add_button],
                        [list_box, edit_button, done_button],
                        [exit_button]],
                    font=("Helvetica",20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            save_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values["todo"]

                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                save_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.popup("Please select an item first.", font=("helvetica", 20))

        case "Done":
            try:
                todo_to_complete = values['todos'][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                save_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                fsg.popup("Please select an item first.", font=("Helvetica", 20))

        case "todos":
            window['todo'].update(value=values["todos"][0])

        case "Exit":
            print("Window closed")
            break

        case fsg.WIN_CLOSED:
            print("WINDOW closed")
            break

window.close()

