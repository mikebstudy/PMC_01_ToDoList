from functions import get_todos, save_todos
import FreeSimpleGUI as FSG

label = FSG.Text("Type in a todo")
input_box = FSG.InputText(tooltip="Enter todo")
add_button = FSG.Button("Add")

win = FSG.Window("ToDo List", layout=[[label],[input_box, add_button]])
win.read()
win.close()

