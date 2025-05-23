from abc import ABC, abstractmethod

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
            return -1
        

class PersonalTask(Task):
    def color_your_task(self) -> str:
        return "Blue"
    

class WorkTask(Task):
    def color_your_task(self) -> str:
        return "Yellow"