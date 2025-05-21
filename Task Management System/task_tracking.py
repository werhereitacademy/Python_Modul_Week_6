from task_management import TaskManagement

class TaskTracking:
    def __init__(self, task_management : TaskManagement):
        self.task_management = task_management
    
    def get_task_status(self, task_id : int) -> None:
        task = self.task_management.get_task_by_id(task_id)
        if task:
            return task.status
    
    def get_task_deadline(self, task_id : int) -> None:
        task = self.task_management.get_task_by_id(task_id)
        if task:
            return task.deadline

    def get_task_color(self, task_id : int) -> None:
        task = self.task_management.get_task_by_id(task_id)
        if task:
            return task.color
