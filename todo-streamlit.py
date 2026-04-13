import streamlit as st
import os

# Configure page
st.set_page_config(
    page_title="My Dark To-Do List",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark purple/black theme
st.markdown("""
<style>
    .main {
        background-color: #090913;
        color: #F7F6FF;
    }
    .stTextInput > div > div > input {
        background-color: #171732;
        color: #F7F6FF;
        border: 1px solid #5C4CE5;
    }
    .stButton > button {
        background-color: #5C4CE5;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 8px 16px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #7A6FF5;
    }
    .task-item {
        background-color: #12122D;
        padding: 8px;
        margin: 4px 0;
        border-radius: 4px;
        border-left: 4px solid #3A4DE6;
    }
    .delete-btn {
        background-color: #3A4DE6;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 4px 8px;
        font-size: 12px;
        margin-left: 8px;
    }
    .delete-btn:hover {
        background-color: #5B6BF7;
    }
    .clear-btn {
        background-color: #6A3CE7;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 8px 16px;
        font-weight: bold;
    }
    .clear-btn:hover {
        background-color: #8A6EF7;
    }
    h1 {
        color: #E8D7FF;
        font-family: 'Segoe UI', sans-serif;
    }
    h3 {
        color: #B8B0F5;
        font-family: 'Segoe UI', sans-serif;
    }
    .task-count {
        color: #F2F0FF;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Constants
TASK_FILE = "tasks.txt"

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Load tasks from file on startup
def load_tasks():
    if os.path.exists(TASK_FILE):
        try:
            with open(TASK_FILE, "r", encoding="utf-8") as file:
                st.session_state.tasks = [line.strip() for line in file if line.strip()]
        except:
            st.warning("Unable to load saved tasks.")

# Save tasks to file
def save_tasks():
    try:
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            for task in st.session_state.tasks:
                file.write(task + "\n")
    except:
        st.error("Unable to save tasks.")

# Load tasks on app start
load_tasks()

# Title and subtitle
st.markdown("<h1>My Dark To-Do List</h1>", unsafe_allow_html=True)
st.markdown("<h3>Purple, blue and black theme</h3>", unsafe_allow_html=True)

# Task counter
st.markdown(f"<div class='task-count'>Number of tasks: {len(st.session_state.tasks)}</div>", unsafe_allow_html=True)

# Add task section
st.subheader("Add New Task")
new_task = st.text_input("Enter a task:", key="new_task_input")

if st.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append(new_task.strip())
        save_tasks()
        st.success("Task added!")
        st.rerun()
    else:
        st.warning("Please enter a task.")

# Display tasks
st.subheader("Your Tasks")

if st.session_state.tasks:
    # Create columns for tasks and delete buttons
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"<div class='task-item'>{task}</div>", unsafe_allow_html=True)
        with col2:
            if st.button("Delete", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                save_tasks()
                st.success("Task deleted!")
                st.rerun()
else:
    st.info("No tasks yet. Add one above!")

# Clear all tasks
st.subheader("Actions")
if st.button("Clear All Tasks", key="clear_all"):
    if st.session_state.tasks:
        st.session_state.tasks.clear()
        save_tasks()
        st.success("All tasks cleared!")
        st.rerun()
    else:
        st.info("No tasks to clear.")