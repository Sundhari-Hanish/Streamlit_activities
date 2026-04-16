import streamlit as st
file_name="tasks.txt"

# load tasks t=from file
def load_tasks():
    try:
        with open(file_name,"r") as file:
            tasks=file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []
    
# save tasks to file
def save_tasks(tasks):
    with open(file_name,"w") as file:
        for task in tasks:
            file.write(task +"\n")

# initialize tasks
tasks=load_tasks()
st.title("Daily task tracker")

# add new task
new_task=st.text_input("Enter a new task")
if st.button("Add task"):
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        st.success("Task added")
    else:
        st.warning("Please enter a task")
st.subheader("Your tasks")

#display tasks
for i, task in enumerate(tasks):
    col1, col2= st.columns([0.8,0.2])
    with col1:
        st.write(f"{i+1}.{task}")
    with col2:
        if st.button("Delete",key=i):
            tasks.pop(i)
            save_tasks(tasks)
            st.experimental_rerun()
