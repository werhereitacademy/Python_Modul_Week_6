from abc import ABC, abstractmethod
from datetime import datetime

class Task(ABC):
    def __init__(self, task_id, task_name,deadline,color="",status="Pending",priority="Low"):
        self.task_id = task_id
        self.task_name = task_name
        self.deadline = deadline
        self.status = status  
        self.priority = priority  
        self.color = color

    @abstractmethod
    def color_your_task(self):
        
        pass

    def days_to_accomplish_task(self):
        """Calculate the number of days left to accomplish the task."""
        today = datetime.now()
        delta = self.deadline - today
        return delta.days

    def __str__(self):
        return (
            f"Task ID: {self.task_id}, Name: {self.task_name}, Deadline: {self.deadline}, "
            f"Status: {self.status}, Priority: {self.priority}, Color: {self.color}")