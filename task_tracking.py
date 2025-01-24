# TASK TRACKING

from task_management import TaskManagement
from task import Task

class TaskTracking:
    def __init__(self, task_management: TaskManagement):
        self.task_management = task_management

    def get_task_status(self, task_id: int) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            print(f"Task {task_id} status: {task.status}")

    def get_task_deadline(self, task_id: int) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            print(f"Task {task_id} deadline: {task.deadline}")

    def get_task_color(self, task_id: int) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            print(f"Task {task_id} color: {task.color}")

    def get_task_by_id(self, task_id: int) -> Task:
        return self.task_management.get_task_by_id(task_id)
    
