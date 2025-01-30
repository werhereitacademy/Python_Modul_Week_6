"""TASK CLASS"""	

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Abstract Base Class (Task)
class Task(ABC):
    def __init__(self,task_id:int, name:str, deadline):
        self.__name = name
        self.__startdate = datetime.now().date()
        self.__deadline = self.process_deadline(deadline)
        self.__task_id = task_id
        self.__status = "Pending"
        self.__priority = "Medium"
        self.__color = ""

    def set_task_id(self, task_id):
        self.__task_id = task_id
    def get_task_id(self):
        return self.__task_id
    
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    
    def set_startdate(self, startdate):
        self.__startdate = startdate
    def get_startdate(self):
        return self.__startdate
    
    def set_deadline(self, deadline):
        self.__deadline = deadline
    def get_deadline(self):
        return self.__deadline
    
    def set_status(self, status):
        self.__status = status
    def get_status(self):
        return self.__status

    def set_priority(self, priority):
        self.__priority = priority
    def get_priority(self):
        return self.__priority

    def set_color(self, color):
        self.__color = color
    def get_color(self):
        return self.__color
    
    def process_deadline(self, deadline):
        SPECIAL_KEYWORDS = {
            "today": datetime.now().date(),
            "tomorrow": (datetime.now() + timedelta(days=1)).date(),
            "next week": (datetime.now() + timedelta(weeks=1)).date(),
            "next month": (datetime.now() + timedelta(days=30)).date(),
            "next year": (datetime.now() + timedelta(days=365)).date(),
        }
        return SPECIAL_KEYWORDS.get(deadline.lower(), deadline)
    
    def get_task_dict(self):
        return {
            "task ID": self.__task_id,
            "Task name": self.__name,
            "Startdate": self.__startdate,
            "Deadline": self.__deadline,
            "Status": self.__status,
            "Priority": self.__priority,
            "Color": self.__color
        }
    
    @abstractmethod
    def display_task(self):
        for i,j in self.get_task_dict().items():
            print(f"{i}: {j}")
    def __str__(self):
        return f"{self.__name} - {self.__startdate} - {self.__deadline} - {self.__status} - {self.__priority} - {self.__color}"
    
    def days_to_deadline(self):
        if  self.__deadline < datetime.now().date():
            return "Deadline has passed"
        elif self.__status == "Completed":
            return "Task is completed"
        elif self.__deadline == datetime.now().date():
            return "Deadline is today"
        else:
            return (self.__deadline - datetime.now().date()).days
        
        