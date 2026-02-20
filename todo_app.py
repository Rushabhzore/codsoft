import tkinter as tk
from tkinter import messagebox
import os

# --- Configuration ---
FILE_NAME = "tasks.txt"

# --- Functions ---
def load_tasks():
    """Loads tasks from the text file into the listbox."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
                # If a task was marked as done previously, make it gray
                if task.strip().endswith("[DONE]"):
                    task_listbox.itemconfig(tk.END, {'fg': 'gray'})

def save_tasks():
    """Saves the current tasks in the listbox to the text file."""
    tasks = task_listbox.get(0, tk.END)
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    """Gets the task from the entry box and adds it to the list."""
    task_text = task_entry.get()
    if task_text.strip() != "":
        task_listbox.insert(tk.END, task_text)
        task_entry.delete(0, tk.END) # Clear the input field
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task first!")

def delete_task():
    """Deletes the selected task from the list."""
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_done():
    """Marks the selected task as completed."""
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_text = task_listbox.get(selected_task_index)
        
        # Check if it's already marked as done
        if not task_text.endswith("[DONE]"):
            # Update the text and color
            updated_text = task_text + " [DONE]"
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, updated_text)
            task_listbox.itemconfig(selected_task_index, {'fg': 'gray'})
            save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")

def clear_all():
    """Clears all tasks from the list."""
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?")
    if confirm:
        task_listbox.delete(0, tk.END)
        save_tasks()

# --- Main UI Setup ---
# Create the main window
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x500")
root.config(bg="#f4f4f4")
root.resizable(False, False)

# --- UI Widgets ---
# Title Label
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#f4f4f4")
title_label.pack(pady=15)

# Input Field (Entry)
task_entry = tk.Entry(root, font=("Helvetica", 14), width=25)
task_entry.pack(pady=10)

# Frame for Listbox and Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

# Scrollbar
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Listbox (The table/list of tasks)
task_listbox = tk.Listbox(
    list_frame, 
    width=35, 
    height=10, 
    font=("Helvetica", 12),
    selectbackground="#a6a6a6",
    yscrollcommand=scrollbar.set
)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=task_listbox.yview)

# Frame for Buttons
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=10)

# Buttons
add_btn = tk.Button(button_frame, text="Add Task", font=("Helvetica", 10), bg="#4caf50", fg="white", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5, pady=5)

done_btn = tk.Button(button_frame, text="Mark Done", font=("Helvetica", 10), bg="#2196f3", fg="white", width=12, command=mark_done)
done_btn.grid(row=0, column=1, padx=5, pady=5)

delete_btn = tk.Button(button_frame, text="Delete Task", font=("Helvetica", 10), bg="#f44336", fg="white", width=12, command=delete_task)
delete_btn.grid(row=1, column=0, padx=5, pady=5)

clear_btn = tk.Button(button_frame, text="Clear All", font=("Helvetica", 10), bg="#ff9800", fg="white", width=12, command=clear_all)
clear_btn.grid(row=1, column=1, padx=5, pady=5)

# --- Startup Action ---
# Load existing tasks when the app starts
load_tasks()

# Run the application
root.mainloop()