from task_management import TaskManagement

class TaskEditing:
    def __init__(self, task_management: TaskManagement):
        self._task_management = task_management

    def set_status(self, task_id, status):
        task = self._task_management.get_task_by_id(task_id)
        if task:
            task.status = status

    def mark_completed(self, task_id):
        self.set_status(task_id, "Completed")

    def set_priority(self, task_id, priority):
        task = self._task_management.get_task_by_id(task_id)
        if task:
            task.priority = priority


