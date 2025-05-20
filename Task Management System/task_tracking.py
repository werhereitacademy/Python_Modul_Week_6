from task_management import TaskManagement

class TaskTracking:
    def __init__(self, task_management : TaskManagement):
        self.task_management = task_management
    
    def get_task_by_id(self, task_id : int):
        for task in self.task_management.task_list:
            if task.task_id == task_id:
                return task
        return None
    
    def get_task_status(self, task_id : int) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            print(f"Status of task {task_id}: {task.status}")
    
    def get_task_deadline(self, task_id : int) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            print(f"Dedline of task {task_id}: {task.deadline}")

    def get_task_color(self, task_id : int) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            print(f"Color of task {task_id}: {task.color}")
