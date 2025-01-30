"""TASK CLASS"""	

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Abstract Base Class (Task)
class Task(ABC):
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = self.process_deadline(deadline)
        self.status = "Pending"
        self.priority = "Medium"

    @abstractmethod
    def display_task(self):
        pass

    def process_deadline(self, deadline):
        SPECIAL_KEYWORDS = {
            "today": datetime.now().date(),
            "tomorrow": (datetime.now() + timedelta(days=1)).date(),
            "next week": (datetime.now() + timedelta(weeks=1)).date(),
        }
        return SPECIAL_KEYWORDS.get(deadline.lower(), deadline)

# mysection