from task import Task
class WorkTask(Task):
    def __init__(self, task_id, task_name, deadline):
        super().__init__(task_id, task_name, deadline)
        self.priority = "High"
        self.color = self.color_your_task()

    def color_your_task(self):
        return "Red"
