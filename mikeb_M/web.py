import streamlit as st
import backend as be

todos = be.load_todos()

def add_todo2():
    new_todo = st.session_state["new_todo"]
    be.add_todo(new_todo)
    st.session_state["new_todo"] = ""

st.title("ToDo List")
st.subheader("Course todo app")
st.write("Increase your productivity!!!")

for idx, todo in enumerate(todos):
    checkbox_setting = st.checkbox(todo["todo"], key=todo)
    if checkbox_setting:
        todos.pop(idx)
        be.save_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add new todo...",
              on_change=add_todo2, key='new_todo')

