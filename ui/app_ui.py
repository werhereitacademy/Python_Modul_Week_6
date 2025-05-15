import tkinter as tk
from tkinter import messagebox
from core.task_management import TaskManagement
from core.task_editing import TaskEditing
from core.task_tracking import TaskTracking
from models.personal_task import PersonalTask
from models.work_task import WorkTask

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager GUI")

        self.tm = TaskManagement()
        self.te = TaskEditing(self.tm)
        self.tt = TaskTracking(self.tm)

        self.task_id = tk.IntVar()
        self.task_name = tk.StringVar()
        self.task_date = tk.StringVar()
        self.task_type = tk.StringVar(value="Personal")

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="ID").pack()
        tk.Entry(self.root, textvariable=self.task_id).pack()
        tk.Label(self.root, text="Name").pack()
        tk.Entry(self.root, textvariable=self.task_name).pack()
        tk.Label(self.root, text="Deadline (YYYY-MM-DD)").pack()
        tk.Entry(self.root, textvariable=self.task_date).pack()

        tk.Label(self.root, text="Type").pack()
        tk.OptionMenu(self.root, self.task_type, "Personal", "Work").pack()

        tk.Button(self.root, text="Add Task", command=self.add_task).pack()
        tk.Button(self.root, text="Show Tasks", command=self.show_tasks).pack()
        tk.Button(self.root, text="Mark Completed", command=self.mark_done).pack()

        self.task_display = tk.Text(self.root, height=15, width=50)
        self.task_display.pack()

    def add_task(self):
        task_id = self.task_id.get()
        name = self.task_name.get()
        deadline = self.task_date.get()
        if self.task_type.get() == "Personal":
            task = PersonalTask(task_id, name, deadline)
        else:
            task = WorkTask(task_id, name, deadline)
        self.tm.add_task(task)
        messagebox.showinfo("Success", "Task Added!")

    def show_tasks(self):
        self.task_display.delete(1.0, tk.END)
        for task in self.tm.get_all_tasks():
            self.task_display.insert(tk.END, str(task) + "\n")

    def mark_done(self):
        task_id = self.task_id.get()
        if self.te.mark_status_completed(task_id):
            messagebox.showinfo("Done", "Task marked as completed!")
        else:
            messagebox.showerror("Error", "Task not found.")