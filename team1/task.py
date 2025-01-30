from abc import ABC, abstractmethod
from datetime import datetime

class Task(ABC):
    def __init__(self, task_id, task_name, deadline, status="Pending", priority="Low", color=None):
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
        return (self.deadline - datetime.now()).days  # datetime modülü içinde datetime adında bir sınıf bulunur.
        
    def __str__(self):  #Bu metodun görevi, görev detaylarını düzgün bir formatta döndürmek.
        return f"Task ID: {self.task_id}, Name: {self.task_name}, Status: {self.status}, Priority: {self.priority}, Deadline: {self.deadline}"
    
class PersonalTask (Task):

    def __init__(self, task_id, task_name, deadline,):
        super().__init__(task_id, task_name, deadline, priority="Low", color="Blue")
    def color_your_task(self):
        return f"The task {self.task_name} is colored in Blue."


class WorkTask (Task):
   
    def __init__(self, task_id, task_name, deadline):
        super().__init__(task_id, task_name, deadline, priority="High", color="Red")
    def color_your_task(self):
        return f"The task {self.task_name} is colored in Red."