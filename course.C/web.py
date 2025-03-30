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

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
