# TASK MANAGEMENT

from typing import List   # List türünü kullanabilmek için gerekli bir import işlemi yapar. 
from datetime import datetime
from task import Task  # Task sınıfını ve alt sınıflarını burada kullanacağız.

class TaskManagement:
    def __init__(self):
        self.task_list: List[Task] = []  
        
    def add_task(self, task: Task) -> None:
        """Yeni bir görev ekler."""
        self.task_list.append(task)
        print(f"Task '{task.task_name}' added successfully.")  


    def display_tasks(self) -> None:
        """Mevcut tüm görevleri görüntüler."""
        if not self.task_list:
            print("No tasks available.")
        else:
            for task in self.task_list:
                print(task)  # Her bir görevin __str__ metodunu çağırır.

    def get_task_by_id(self, task_id: int) -> Task:
        """Verilen task_id'ye sahip görevi döndürür."""
        for task in self.task_list:
            if task.task_id == task_id:
                return task
        return None
