from datetime import datetime

# Base Task class
class Task:
    def __init__(self, task_id, name, deadline):
        self.task_id = task_id
        self.name = name
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.status = "Pending"
        self.priority = "Normal"

    def remaining_days(self):
        return (self.deadline - datetime.now()).days

    def get_color(self):
        if self.status == "Completed":
            return "Blue"
        days_left = self.remaining_days()
        if days_left <= 3:
            return "Red"
        elif days_left <= 7:
            return "Orange"
        else:
            return "Red" if self.status == "Pending" else "Green"

    def __str__(self):
        return (f"Task ID: {self.task_id}, Name: {self.name}, Deadline: {self.deadline.date()}, "
                f"Color: {self.get_color()}, Status: {self.status}, Priority: {self.priority}, "
                f"Remaining Days: {self.remaining_days()}")

class PersonalTask(Task):
    pass

class WorkTask(Task):
    pass

# Task Management
class TaskManagement:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.task_id] = task

    def display_tasks(self):
        for task in self.tasks.values():
            print(task)

# Editing
class TaskEditing:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def task_status(self, task_id, status):
        if task_id in self.task_manager.tasks:
            self.task_manager.tasks[task_id].status = status

    def status_completed(self, task_id):
        if task_id in self.task_manager.tasks:
            self.task_manager.tasks[task_id].status = "Completed"

    def prioritization(self, task_id, priority):
        if task_id in self.task_manager.tasks:
            self.task_manager.tasks[task_id].priority = priority

# Tracking
class TaskTracking:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def task_deadline(self, task_id):
        if task_id in self.task_manager.tasks:
            return self.task_manager.tasks[task_id].deadline

    def task_color(self, task_id):
        if task_id in self.task_manager.tasks:
            color = self.task_manager.tasks[task_id].get_color()
            print(f"Task with ID {task_id}'s color is {color}.")
            return color
        return None

# My_tasks
lezen_b2 = TaskManagement()
E_lazen = TaskEditing(lezen_b2)
T_lazen = TaskTracking(lezen_b2)

# follow my task
grammar = PersonalTask(1, "grammar", "2025-06-13")
words = WorkTask(2, "words", "2025-06-20")
lezen_b2.add_task(grammar)
lezen_b2.add_task(words)

# states
E_lazen.task_status(1, "Completed")
E_lazen.prioritization(1, "high")
E_lazen.prioritization(2, "low")

T_lazen.task_color(2)
lezen_b2.display_tasks()
