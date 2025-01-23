from abc import ABC, abstractmethod
from datetime import datetime

class Task(ABC):
    def __init__(self, task_id, task_name, deadline, color=None, status="Pending", priority="Low"):
        self.task_id = task_id
        self.task_name = task_name
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.status = status
        self.priority = priority
        self.color = color

    @abstractmethod 
    def color_your_task(self): 
        pass

    def days_to_accomplish_task(self):
        today = datetime.today()
        return (self.deadline - today).days 
        
    def __str__(self): 
        return f"id:{self.task_id}, task name:{self.task_name}, deadline:{self.deadline}, task color:{self.color}, task status:{self.status}, task priority:{self.priority}, remaining days:{self.days_to_accomplish_task()}"



class PersonalTask(Task):
    def __init__(self, task_id, task_name, deadline):
        super().__init__(task_id, task_name, deadline)
        self.color = "blue" 

    def color_your_task(self): 
        self.color = "blue" 
    
class WorkTask(Task):
    def __init__(self, task_id, task_name, deadline):
        super().__init__(task_id, task_name, deadline)
        self.priority = "high"
        self.color = "red"
        
    def color_your_task(self):
        self.color = "red"