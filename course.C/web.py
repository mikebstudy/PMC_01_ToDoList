import streamlit as st
from functions import get_todos, save_todos

st.title("ToDo List")
st.subheader("Course todo app")
st.write("Increase your productivity!!!")

todos = get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new todo...")
