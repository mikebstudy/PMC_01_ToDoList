import streamlit as st
import todo_backend as backend


def main():
    st.title("📝 To-Do List Web App")

    todo_list = backend.load_todo_list()

    # Display existing tasks
    st.subheader("Your Tasks:")
    for i, task in enumerate(todo_list):
        st.write(f"{i + 1}. **[{task['priority'].capitalize()}]** {task['task']}")

    # Add a new task
    with st.form("add_task_form"):
        new_task = st.text_input("Enter a new task:")
        priority = st.selectbox("Select priority:", ["high", "medium", "low"])
        submitted = st.form_submit_button("Add Task")
        if submitted and new_task:
            backend.add_task(todo_list, new_task, priority)
            st.success("Task added successfully!")
            st.rerun()

    # Edit a task
    with st.form("edit_task_form"):
        task_number = st.number_input("Enter task number to edit:", min_value=1, max_value=len(todo_list), step=1)
        new_task = st.text_input("New task name:")
        new_priority = st.selectbox("New priority:", ["high", "medium", "low"])
        edit_submitted = st.form_submit_button("Edit Task")
        if edit_submitted and new_task:
            if backend.edit_task(todo_list, task_number - 1, new_task, new_priority):
                st.success("Task edited successfully!")
                st.rerun()
            else:
                st.error("Invalid task number.")

    # Remove a task
    with st.form("remove_task_form"):
        remove_task_number = st.number_input("Enter task number to remove:", min_value=1, max_value=len(todo_list),
                                             step=1)
        remove_submitted = st.form_submit_button("Remove Task")
        if remove_submitted:
            if backend.remove_task(todo_list, remove_task_number - 1):
                st.success("Task removed successfully!")
                st.rerun()
            else:
                st.error("Invalid task number.")

    # Reorder a task
    with st.form("reorder_task_form"):
        old_position = st.number_input("Enter current task number:", min_value=1, max_value=len(todo_list), step=1)
        new_position = st.number_input("Enter new position:", min_value=1, max_value=len(todo_list), step=1)
        reorder_submitted = st.form_submit_button("Reorder Task")
        if reorder_submitted:
            if backend.reorder_task(todo_list, old_position - 1, new_position - 1):
                st.success("Task reordered successfully!")
                st.rerun()
            else:
                st.error("Invalid positions.")

    # Sort tasks by priority
    if st.button("Sort by Priority"):
        backend.sort_by_priority(todo_list)
        st.success("Tasks sorted by priority.")
        st.rerun()


if __name__ == "__main__":
    main()
