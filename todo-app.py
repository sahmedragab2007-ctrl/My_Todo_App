import tkinter as tk
from tkinter import messagebox

TASK_FILE = "tasks.txt"
tasks = []

root = tk.Tk()
root.title("To-Do App")
root.configure(bg="#090913")
root.geometry("420x520")
root.resizable(False, False)

header_frame = tk.Frame(root, bg="#101026")
header_frame.pack(fill=tk.X, padx=16, pady=(16, 8))

title_label = tk.Label(
    header_frame,
    text="My Dark To-Do List",
    font=("Segoe UI", 20, "bold"),
    fg="#E8D7FF",
    bg="#101026",
)
title_label.pack(anchor="w")

subtitle_label = tk.Label(
    header_frame,
    text="Purple, blue and black theme",
    font=("Segoe UI", 10),
    fg="#B8B0F5",
    bg="#101026",
)
subtitle_label.pack(anchor="w", pady=(4, 0))

count_frame = tk.Frame(root, bg="#090913")
count_frame.pack(fill=tk.X, padx=16, pady=(0, 12))

tasks_count_label = tk.Label(
    count_frame,
    text="Number of tasks: 0",
    font=("Segoe UI", 11, "bold"),
    fg="#F2F0FF",
    bg="#090913",
)
tasks_count_label.pack(anchor="w")

entry_frame = tk.Frame(root, bg="#090913")
entry_frame.pack(fill=tk.X, padx=16, pady=(0, 12))

entry = tk.Entry(
    entry_frame,
    width=28,
    font=("Segoe UI", 12),
    bg="#171732",
    fg="#F7F6FF",
    insertbackground="#F7F6FF",
    relief=tk.FLAT,
)
entry.pack(side=tk.LEFT, ipady=8, padx=(0, 8))

add_btn = tk.Button(
    entry_frame,
    text="Add Task",
    command=lambda: add_task(),
    bg="#5C4CE5",
    fg="white",
    activebackground="#7A6FF5",
    activeforeground="white",
    font=("Segoe UI", 10, "bold"),
    relief=tk.FLAT,
    width=12,
)
add_btn.pack(side=tk.LEFT)

listbox_frame = tk.Frame(root, bg="#12122D")
listbox_frame.pack(fill=tk.BOTH, expand=True, padx=16, pady=(0, 12))

listbox = tk.Listbox(
    listbox_frame,
    width=40,
    height=12,
    font=("Segoe UI", 11),
    bg="#12122D",
    fg="#E7E4FF",
    selectbackground="#3B3CE8",
    selectforeground="white",
    activestyle="none",
    bd=0,
    highlightthickness=0,
)
listbox.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)

buttons_frame = tk.Frame(root, bg="#090913")
buttons_frame.pack(fill=tk.X, padx=16, pady=(0, 16))

delete_button = tk.Button(
    buttons_frame,
    text="Delete Selected",
    command=lambda: delete_task(),
    bg="#3A4DE6",
    fg="white",
    activebackground="#5B6BF7",
    activeforeground="white",
    font=("Segoe UI", 10, "bold"),
    relief=tk.FLAT,
    width=18,
)
delete_button.pack(side=tk.LEFT, padx=(0, 8))

clear_btn = tk.Button(
    buttons_frame,
    text="Clear All",
    command=lambda: clear_all(),
    bg="#6A3CE7",
    fg="white",
    activebackground="#8A6EF7",
    activeforeground="white",
    font=("Segoe UI", 10, "bold"),
    relief=tk.FLAT,
    width=12,
)
clear_btn.pack(side=tk.LEFT)


def update_count():
    count = len(tasks)
    tasks_count_label.config(text=f"Number of tasks: {count}")


def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
        update_count()


def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
        save_tasks()
        update_count()


def clear_all():
    answer = messagebox.askyesno("Confirmation", "Are you sure you want to delete all tasks?")
    if answer:
        listbox.delete(0, tk.END)
        tasks.clear()
        save_tasks()
        update_count()


def save_tasks():
    try:
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
    except OSError:
        messagebox.showerror("Error", "Unable to save tasks.")


def load_tasks():
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
                    listbox.insert(tk.END, task)
        update_count()
    except FileNotFoundError:
        pass
    except OSError:
        messagebox.showwarning("Warning", "Unable to load saved tasks.")

load_tasks()
root.mainloop()
root.title("To_Do App love")
root.configure(bg="#0A0A0A")

tasks_count_label = tk.Label(root, text="Number of tasks: 0",font=("Arial 10 bold"), bg="#e73ce7")
tasks_count_label.pack(pady=5)

entry = tk.Entry(root,width=30, font="Arial 12")
entry.pack(pady=10)

add_btn = tk.Button(root,text="Add Task",command=add_task, bg="#e73c3c" , fg="white", font="Arial 10 bold",width=20)
add_btn.pack()
 
listbox = tk.Listbox(root,width=40, height=10, font="Arial 11")
listbox.pack(pady=10)

delete_button = tk.Button(root,text="Delete Selected Task", command=delete_task, bg="#3c6ae7", fg="white" , font="Arial 10 bold",width=20)
delete_button.pack(pady=5)

clear_btn = tk.Button(root,text="Clear All Tasks",command=clear_all, bg="#6a3ce7", fg="white",font="Arial 10 bold",width=20)
clear_btn.pack(pady=5)

load_tasks()
root.mainloop()