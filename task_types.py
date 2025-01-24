from task import Task

class PersonalTask(Task):
    def __init__(self, task_id, task_name, deadline):
        super().__init__(task_id, task_name, deadline)

    def color_your_task(self): 
        color = self.color = "blue" 
        return color
    
class WorkTask(Task):
    def __init__(self, task_id, task_name, deadline):
        super().__init__(task_id, task_name, deadline)
        self.priority = "high"
        
    def color_your_task(self):
        color = self.color = "red"
        return color