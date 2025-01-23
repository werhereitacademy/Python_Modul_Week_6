from typing import List  # For using the List type
from datetime import datetime 
from task import Task  # Task class to manage tasks

class TaskManagement:
    def __init__(self):
        # Initialize an empty task list
        self.task_list: List[Task] = []

    def add_task(self, task: Task) -> None:
        # Add a task to the list
        self.task_list.append(task)
        print(f"Task '{task.task_name}' added successfully.")

    def display_tasks(self) -> None:
        # Display all tasks or notify if empty
        if not self.task_list:
            print("No tasks available.")
        else:
            for task in self.task_list:
                print(task)  # Assumes Task has a __str__ method
