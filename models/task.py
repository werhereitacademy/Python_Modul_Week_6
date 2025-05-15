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

    def __str__(self):
        return f"{self.task_id}: {self.task_name} | {self.status} | {self.priority} | {self.deadline.date()}"