from functions import get_todos, save_todos
import FreeSimpleGUI as FSG

label = FSG.Text("Type in a todo")
input_box = FSG.InputText(tooltip="Enter todo", key="todo")
add_button = FSG.Button("Add")
list_box = FSG.Listbox(values=get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = FSG.Button("Edit")

win = FSG.Window("ToDo List",
                 layout=[[label],[input_box, add_button], [list_box, edit_button]],
                 font=("Helvetica",20))

while True:
    event, values = win.read()
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            save_todos(todos)
            win['todos'].update(values=todos)

        case "Edit":
            print("Edit button")
            todo_to_edit = values['todos'][0]
            new_todo = values["todo"]

            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            save_todos(todos)
            win['todos'].update(values=todos)

        case "todos":
            win['todo'].update(value=values["todos"][0])

        case FSG.WIN_CLOSED:
            break

win.close()

