from abc import ABC, abstractmethod
from datetime import datetime

class Task(ABC):  # Soyut sınıf
    def __init__(self, task_id, task_name, deadline):
        self.task_id = task_id
        self.task_name = task_name
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.status = "Pending"
        self.priority = "Low"
        self.color = ""

    @abstractmethod
    def color_your_task(self):  # Soyut metod
        pass

    def __str__(self):
        remaining_days = (self.deadline - datetime.now()).days
        return f"Task ID: {self.task_id}, Name: {self.task_name}, Deadline: {self.deadline.date()}, Color: {self.color}, Status: {self.status}, Priority: {self.priority}, Remaining Days: {remaining_days}"
