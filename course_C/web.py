import streamlit as st
from functions import get_todos, save_todos

todos = get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    save_todos(todos)
    st.session_state["new_todo"] = ""


st.title("ToDo List")
st.subheader("Course todo app")
st.write("Increase your productivity!!!")

for idx, todo in enumerate(todos):
    checkbox_setting = st.checkbox(todo, key=todo)
    if checkbox_setting:
        todos.pop(idx)
        save_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="",placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

