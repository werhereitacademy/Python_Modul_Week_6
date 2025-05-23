from abc import ABC, abstractmethod
from datetime import datetime

class Task(ABC):         #soyut sinif
    def __init__(self, task_id: int, task_name: str, deadline: str, status: str, priority: str):
        self.task_id = task_id
        self.task_name = task_name
        self.deadline = deadline
        self.status = status
        self.priority = priority
        self.color = self.color_your_task()


    @abstractmethod
    def color_your_task(self) -> str:
        pass

    def days_to_accomplish_task(self) -> int:
        today = datetime.today()
        try:
            deadline_date = datetime.strptime(self.deadline, "%Y-%m-%d")
            return (deadline_date - today).days
        except ValueError:
            return -1
        

class PersonalTask(Task):
    def color_your_task(self) -> str:
        return "Blue"
    

class WorkTask(Task):
    def color_your_task(self) -> str:
        return "Yellow"