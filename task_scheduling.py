from datetime import datetime, timedelta
from tasks import PersonalTask ,WorkTask

SPECIAL_KEYWORDS = {
    "today": datetime.now().date(),
    "tomorrow": datetime.now().date() + timedelta(days=1),
    "next week": datetime.now().date() + timedelta(weeks=1)}

def get_due_date(keyword):
    return SPECIAL_KEYWORDS.get(keyword.lower(), None)

class TaskScheduling:
    def __init__(self, task_management):
        self.task_management = task_management

    def create_task(self, id, type, name, priority, due_date):
        
            if type=='personal':
                task = PersonalTask(id, type, name, priority, due_date)
            
            elif type=='work':
                task = WorkTask(id, type, name, priority, due_date)  
            else:
                 raise ValueError("Unknown task type.")
            self.task_management.add_task(task)
        
            