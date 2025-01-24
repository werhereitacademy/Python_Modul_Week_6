class TaskTracking:
    def __init__(self, task_management):
        self.task_management = task_management

    def get_task_status(self, task_id):
        task = self.get_task_by_id(task_id)
        return task.status if task else None
        

    def get_task_deadline(self, task_id):
        task = self.get_task_by_id(task_id)
        return task.deadline.date() if task else None
        

    def get_task_color(self, task_id):
        task = self.get_task_by_id(task_id)
        return task.color if task else None
        

    def get_task_by_id(self, task_id):
        for task in self.task_management.task_list:
            if task.task_id == task_id:
                return task
            else:
                return None
  