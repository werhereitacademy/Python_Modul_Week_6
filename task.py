from abc import ABC, abstractmethod  #Selin
from datetime import datetime

class Task(ABC):
    def __init__(self, task_id,task_name,task_deadline, task_status='pending',task_priority='medium', task_color='orange' ):
        self.task_id=task_id
        self.task_name=task_name
        self.task_deadline=task_deadline
        self.task_status=task_status
        self.task_priority=task_priority
        self.task_color=task_color
        
    def days_left(self):
        today=datetime.now().date()
        return (self.task_deadline.date() - today).days

    def auto_set_color(self):
        if self.task_status == 'done':
            self.task_color = 'green'
        elif self.task_status == 'late':
            self.task_color = 'red'
        elif self.task_status == 'atf':
            self.task_color = 'gray'
        else:
            self.task_color = 'orange'
    
    @abstractmethod
    def color_your_task(self, color):
        pass
    
class PersonalTask(Task):
    def __init__(self, task_id, task_name, task_deadline, task_status='pending', task_priority='low', task_color='orange'):
        super().__init__(task_id, task_name, task_deadline, task_status, task_priority, task_color)
    
    def auto_set_color(self):
        if self.task_status == 'done':
            self.task_color = 'green'
        elif self.task_status == 'late':
            self.task_color = 'red'
        elif self.task_status == 'atf':
            self.task_color = 'gray'
        else:
            self.task_color = 'orange'
    
    def color_your_task(self, color):
        self.task_color=color

class WorkTask(Task):
    def __init__(self, task_id, task_name, task_deadline, task_status='pending', task_priority='high', task_color='orange'):
        super().__init__(task_id, task_name, task_deadline, task_status, task_priority, task_color)
    
    def auto_set_color(self):
        if self.task_status == 'done':
            self.task_color = 'green'
        elif self.task_status == 'late':
            self.task_color = 'red'
        elif self.task_status == 'atf':
            self.task_color = 'gray'
        else:
            self.task_color = 'orange'
    
    def color_your_task(self, color):
        self.task_color=color



'''
Red: late
Orange: in progress (pending)
Gray: coming soon
Green: finished
'''