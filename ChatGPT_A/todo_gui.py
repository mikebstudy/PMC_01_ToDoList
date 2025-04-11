import FreeSimpleGUI as sg
import todo_backend as backend


def update_task_list(window, todo_list):
    """Update the task list display."""
    window["-TASKS-"].update(values=[f"[{task['priority'].capitalize()}] {task['task']}" for task in todo_list])


def main():
    todo_list = backend.load_todo_list()

    sg.theme("DarkBlue3")

    layout = [
        [sg.Text("To-Do List", font=("Helvetica", 16), justification="center")],
        [sg.Listbox(values=[], size=(40, 10), key="-TASKS-", enable_events=True)],
        [sg.Text("Task:"), sg.InputText(key="-TASK-"), sg.Text("Priority:"),
         sg.Combo(["high", "medium", "low"], key="-PRIORITY-", default_value="medium")],
        [sg.Button("Add"), sg.Button("Edit"), sg.Button("Remove"), sg.Button("Reorder"), sg.Button("Sort"),
         sg.Button("Exit")],
    ]

    window = sg.Window("To-Do List", layout,finalize=True)

    update_task_list(window, todo_list)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        elif event == "Add":
            task = values["-TASK-"].strip()
            priority = values["-PRIORITY-"]
            if task:
                backend.add_task(todo_list, task, priority)
                update_task_list(window, todo_list)
        elif event == "Edit":
            selected_task = values["-TASKS-"]
            if selected_task:
                index = window["-TASKS-"].get_indexes()[0]
                new_task = sg.popup_get_text("Edit Task", default_text=todo_list[index]["task"])
                if new_task:
                    new_priority = sg.popup_get_text("New Priority (high, medium, low)",
                                                     default_text=todo_list[index]["priority"])
                    if new_priority in backend.PRIORITY_ORDER:
                        backend.edit_task(todo_list, index, new_task, new_priority)
                        update_task_list(window, todo_list)
        elif event == "Remove":
            selected_task = values["-TASKS-"]
            if selected_task:
                index = window["-TASKS-"].get_indexes()[0]
                backend.remove_task(todo_list, index)
                update_task_list(window, todo_list)
        elif event == "Reorder":
            selected_task = values["-TASKS-"]
            if selected_task:
                index = window["-TASKS-"].get_indexes()[0]
                new_position = sg.popup_get_text("Enter new position (1-based index)")
                if new_position and new_position.isdigit():
                    new_position = int(new_position) - 1
                    backend.reorder_task(todo_list, index, new_position)
                    update_task_list(window, todo_list)
        elif event == "Sort":
            backend.sort_by_priority(todo_list)
            update_task_list(window, todo_list)

    window.close()


if __name__ == "__main__":
    main()
