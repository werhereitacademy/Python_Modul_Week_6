from datetime import datetime

class TaskEditing:
    def __init__(self, task_management):
        self.task_management = task_management

    def set_task_status(self, task_id, status):
        task = self.get_task_by_id(task_id)
        if task:
            task.status = status
            return status
        else:
            return None
       

    def set_prioritization(self, task_id, priority):
        task = self.get_task_by_id(task_id)
        if task:
            task.priority = priority
            return priority
        else:
            return None

    def set_new_date(self, task_id, deadline):
        task = self.get_task_by_id(task_id)
        if task:
            task.deadline = datetime.strptime(deadline, "%Y-%m-%d")
            return task.deadline
        else:
            return None

    def mark_status_completed(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.status = "Completed"
            return task.status
        else:
            return None

    def get_task_by_id(self, task_id):
        for task in self.task_management.task_list:
            if task.task_id == task_id:
                return task
            else:
                return None
