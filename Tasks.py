
from task import Task

class WorkTask(Task):
    def __init__(self, task_id, task_name, deadline):
        super().__init__(task_id, task_name, deadline,color="",status="Pending", priority = "High")
    
    def color_your_task(self):
        self.color = "Red"

class PersonalTask(Task):
    def __init__(self, task_id, task_name, deadline):
        super().__init__(task_id, task_name, deadline,color="", status="Pending", priority = "Low")
        
    
    def color_your_task(self):
        self.color = "Blue"

