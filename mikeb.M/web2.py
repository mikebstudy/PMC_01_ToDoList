import streamlit as st
import time
import backend as be

st.set_page_config(page_title="ToDo App", layout="centered")

# Exit handling (before anything renders)
if st.session_state.get("exiting"):
    st.markdown("### 👋 Thanks for using the ToDo app!")
    countdown = st.empty()
    for i in range(5, 0, -1):
        countdown.markdown(f"Resuming in **{i}** seconds...")
        time.sleep(1)
    st.session_state["exiting"] = False
    st.rerun()

# Load todos from session or backend
if "todos" not in st.session_state:
    st.session_state.todos = be.load_todos()

# App title
st.title("✅ ToDo App")

# Build task display list
todo_texts = [todo["todo"] for todo in st.session_state.todos]

# Determine which task should be selected by default
if "focus_index" in st.session_state:
    default_index = st.session_state.focus_index
    st.session_state.pop("focus_index")  # one-time use
else:
    default_index = 0

selected_index = None
selected_text = ""

# Show radio if tasks exist
if todo_texts:
    selected_index = st.radio(
        "Select a task:",
        options=range(len(todo_texts)),
        format_func=lambda i: todo_texts[i],
        index=default_index
    )
    st.session_state.selected_task = selected_index  # Save manually
    selected_text = todo_texts[selected_index]

# Clear one-time focus index
# st.session_state.pop("focus_index", None)

# Set up the text input based on selected item
if "todo_input" not in st.session_state:
    st.session_state.todo_input = ""

if selected_text:
    st.session_state.todo_input = selected_text

todo_input = st.text_input("Enter a task:", value=st.session_state.todo_input, key="todo_input_field")

# Buttons in three columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Add"):
        task = todo_input.strip()
        if task:
            be.add_todo(task)
            st.session_state.todos = be.load_todos()
            st.session_state["focus_index"] = len(st.session_state.todos) - 1  # focus new item
            st.rerun()

with col2:
    if st.button("Edit"):
        if selected_index is not None:
            new_task = todo_input.strip()
            if new_task:
                be.update_todo(selected_index, new_task)
                st.session_state.todos = be.load_todos()
                # Save focus index before rerun
                st.session_state.focus_index = selected_index
                st.rerun()

# Drop button (single column below)
with col3:
    if st.button("Drop"):
        if selected_index is not None:
            be.drop_todo(selected_index)
            st.session_state.todos = be.load_todos()
            st.rerun()

# Drop button (single column below)
with col4:
    if st.button("Done"):
        if selected_index is not None:
            be.drop_todo(selected_index)
            st.session_state.todos = be.load_todos()
            st.rerun()

# Exit button
st.markdown("---")
if st.button("🚪 Exit"):
    st.session_state["exiting"] = True
    st.rerun()
