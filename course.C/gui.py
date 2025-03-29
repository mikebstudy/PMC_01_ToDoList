from functions import get_todos, save_todos
import FreeSimpleGUI as FSG

label = FSG.Text("Type in a todo")
input_box = FSG.InputText(tooltip="Enter todo", key="todo")
add_button = FSG.Button("Add")

win = FSG.Window("ToDo List",
                 layout=[[label],[input_box, add_button]],
                 font=("Helvetica",20))

while True:
    event, values = win.read()
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            save_todos(todos)
        case FSG.WIN_CLOSED:
            break

win.close()

