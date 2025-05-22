from task_management import TaskManagement

class TaskTracking:
    def __init__(self, task_management: TaskManagement):
        self._task_management = task_management

    def get_deadline(self, task_id):
        task = self._task_management.get_task_by_id(task_id)
        return task.deadline if task else None

    def get_color(self, task_id):
        task = self._task_management.get_task_by_id(task_id)
        return task.color if task else None