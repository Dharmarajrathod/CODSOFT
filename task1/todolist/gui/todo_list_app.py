import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from task import Task
import json
import os
import csv

DATA_FILE_JSON = '../data/tasks.json'
DATA_FILE_CSV = '../data/tasks.csv'

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Configure the root window
        self.root.geometry('500x500')
        self.root.resizable(False, False)
        self.root.configure(bg='#f5f5f5')

        # Style configuration
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12), padding=10)
        style.configure('TLabel', font=('Helvetica', 12))
        style.configure('TFrame', background='#f5f5f5')
        style.configure('TEntry', font=('Helvetica', 12))

        # Title and Description
        title_frame = ttk.Frame(self.root)
        title_frame.pack(pady=10)
        self.title_label = ttk.Label(title_frame, text="Title")
        self.title_label.grid(row=0, column=0, padx=5)
        self.title_entry = ttk.Entry(title_frame, width=40)
        self.title_entry.grid(row=0, column=1, padx=5)

        description_frame = ttk.Frame(self.root)
        description_frame.pack(pady=10)
        self.description_label = ttk.Label(description_frame, text="Description")
        self.description_label.grid(row=0, column=0, padx=5)
        self.description_entry = ttk.Entry(description_frame, width=40)
        self.description_entry.grid(row=0, column=1, padx=5)

        # Add Task Button
        self.add_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=10)

        # Task Listbox
        self.tasks_listbox = tk.Listbox(self.root, font=('Helvetica', 12), height=10, width=50, bg='#ffffff')
        self.tasks_listbox.pack(pady=10)

        # Bottom Buttons
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(pady=10)
        self.complete_button = ttk.Button(buttons_frame, text="Mark Complete", command=self.mark_task_complete)
        self.complete_button.grid(row=0, column=0, padx=5)
        self.delete_button = ttk.Button(buttons_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

        self.tasks = []
        self.load_tasks()

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        if title:
            task = Task(title, description)
            self.tasks.append(task)
            self.update_task_listbox()
            self.title_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Input Error", "Title is required")

    def mark_task_complete(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index].completed = True
            self.update_task_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Selection Error", "No task selected")

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_task_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Selection Error", "No task selected")

    def update_task_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task.completed else "✗"
            self.tasks_listbox.insert(tk.END, f"[{status}] {task.title}: {task.description}")

    def save_tasks(self):
        self.save_tasks_to_json()
        self.save_tasks_to_csv()

    def save_tasks_to_json(self):
        with open(DATA_FILE_JSON, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file, indent=4)

    def save_tasks_to_csv(self):
        with open(DATA_FILE_CSV, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'description', 'completed'])
            for task in self.tasks:
                writer.writerow([task.title, task.description, task.completed])

    def load_tasks(self):
        self.load_tasks_from_json()
        # Alternatively, you can choose to load from CSV
        # self.load_tasks_from_csv()

    def load_tasks_from_json(self):
        if os.path.exists(DATA_FILE_JSON):
            with open(DATA_FILE_JSON, 'r') as file:
                try:
                    tasks_data = json.load(file)
                    self.tasks = [Task(**data) for data in tasks_data]
                    self.update_task_listbox()
                except json.JSONDecodeError:
                    self.tasks = []

    def load_tasks_from_csv(self):
        if os.path.exists(DATA_FILE_CSV):
            with open(DATA_FILE_CSV, 'r') as file:
                reader = csv.DictReader(file)
                self.tasks = []
                for row in reader:
                    task = Task(row['title'], row['description'])
                    task.completed = row['completed'] == 'True'
                    self.tasks.append(task)
                self.update_task_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
