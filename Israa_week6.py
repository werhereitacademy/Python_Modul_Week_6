from abc import ABC, abstractmethod
from datetime import datetime


class Task(ABC):
    def __init__(self, task_id, task_name, deadline):
        self.task_id = task_id
        self.task_name = task_name
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.status = "Pending"
        self.priority = "Low"
        self.color = ""
    
    @abstractmethod
    def color_your_task(self):
        pass

    def days_to_accomplish_task(self):
        return (self.deadline - datetime.today()).days

    def __str__(self):
        return (f"Task ID: {self.task_id}, Name: {self.task_name}, Deadline: {self.deadline.date()}, "
                f"Color: {self.color}, Status: {self.status}, Priority: {self.priority}, "
                f"Remaining Days: {self.days_to_accomplish_task()}")



class PersonalTask(Task):
    def __init__(self, task_id, task_name, deadline):
        super().__init__(task_id, task_name, deadline)
        self.priority = "Low"
        self.color_your_task()

    def color_your_task(self):
        self.color = "Blue"

class WorkTask(Task):
    def __init__(self, task_id, task_name, deadline):
        super().__init__(task_id, task_name, deadline)
        self.priority = "High"
        self.color_your_task()

    def color_your_task(self):
        self.color = "Red"

class TaskManagement:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def display_tasks(self):
        for task in self.task_list:
            print(task)

class TaskEditing:
    def __init__(self, task_management):
        self.task_management = task_management

    def set_task_status(self, task_id, status):
        task = self.get_task_by_id(task_id)
        task.status = status

    def set_prioritization(self, task_id, priority):
        task = self.get_task_by_id(task_id)
        task.priority = priority

    def set_new_date(self, task_id, deadline):
        task = self.get_task_by_id(task_id)
        task.deadline = datetime.strptime(deadline, "%Y-%m-%d")

    def mark_status_completed(self, task_id):
        task = self.get_task_by_id(task_id)
        task.status = "Completed"
        return True

    def get_task_by_id(self, task_id):
        for task in self.task_management.task_list:
            if task.task_id == task_id:
                return task
        raise ValueError("Task not found.")


class TaskTracking:
    def __init__(self, task_management):
        self.task_management = task_management

    def get_task_status(self, task_id):
        task = self.get_task_by_id(task_id)
        print(f"Task {task_id} Status: {task.status}")

    def get_task_deadline(self, task_id):
        task = self.get_task_by_id(task_id)
        print(f"Task {task_id} Deadline: {task.deadline.date()}")

    def get_task_color(self, task_id):
        task = self.get_task_by_id(task_id)
        print(f"Task with ID {task_id}'s color is {task.color}.")

    def get_task_by_id(self, task_id):
        for task in self.task_management.task_list:
            if task.task_id == task_id:
                return task
        raise ValueError("Task not found.")

# ------------------- Main -------------------

if __name__ == "__main__":
    
    t1 = TaskManagement()
    te = TaskEditing(t1)
    tt = TaskTracking(t1)

  
    p1 = PersonalTask(1, "P1", "2025-03-20")
    w2 = WorkTask(2, "W2", "2025-02-25")
    t1.add_task(p1)
    t1.add_task(w2)

    te.set_task_status(1, "In Progress")
    te.mark_status_completed(1)
    te.set_prioritization(1, "Not Important")

    tt.get_task_color(2)
    t1.display_tasks()
