from abc import ABC, abstractmethod
from datetime import datetime

class Task(ABC):
    def __init__(self, id, type, name, priority, due_date):
        self.id = id  
        self.type=type
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.status = "Pending"  # Başlangıç durumu

    @abstractmethod
    def display_task(self):
        pass

    def mark_as_complete(self):
        self.status = "Completed"
        print(f"Görev tamamlandı: {self.name}")


class PersonalTask(Task):
    def __init__(self, id, type, name, priority, due_date, personal_note=''):
        super().__init__(id, type, name, priority, due_date)
        self.personal_note = personal_note

    def display_task(self):
        return (f"Personal Task - ID: {self.id},Tip: {self.type} İsim: {self.name}, Öncelik: {self.priority}, "
                f"Bitis: {self.due_date}, Not: {self.personal_note}, Durum: {self.status}")       





class WorkTask(Task):
    def __init__(self, id, type, name, priority, due_date):
        super().__init__(id, type, name, priority, due_date)

    def display_task(self):
        return (f"Work Task - ID: {self.task_id},Tip: {self.type}, İsim: {self.name}, Öncelik: {self.priority}, "
                f"Bitis: {self.due_date}, Durum: {self.status}")       