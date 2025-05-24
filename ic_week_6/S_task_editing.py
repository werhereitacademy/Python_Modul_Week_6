from datetime import datetime

class TaskEditing:
    def __init__(self, task_management):
        self.task_management = task_management

    def get_task_by_id(self, task_id):
        for task in self.task_management.task_list:
            if task.task_id == task_id:
                return task
        return None

    def set_task_status(self, task_id, status):
        task = self.get_task_by_id(task_id)
        if task:
            task.status = status

    def set_prioritization(self, task_id, priority):
        task = self.get_task_by_id(task_id)
        if task:
            task.priority = priority

    def set_new_date(self, task_id, deadline):
        task = self.get_task_by_id(task_id)
        if task:
            task.deadline = datetime.strptime(deadline, "%Y-%m-%d")

    def mark_status_completed(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.status = "Completed"
            return True
        return False
