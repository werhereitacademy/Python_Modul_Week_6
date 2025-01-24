from task_management import TaskManagement
from task import Task
from datetime import datetime

"""
TaskEditing sınıfı, bir görev üzerinde düzenleme işlemleri yapmayı sağlayan bir sınıftır. 
Bu sınıf, görevlerin durumunu (status), önceliğini (priority), son tarihini (deadline) güncellemeyi 
ve görevi tamamlanmış olarak işaretlemeyi amaçlayan metotlar içerir. 
TaskEditing sınıfı, görevlerle ilgili bu düzenlemeleri yapmak için TaskManagement sınıfından 
görev bilgilerine erişir
"""


class TaskEditing:
    def __init__(self, task_management: TaskManagement):
        self.task_management = task_management


    def set_task_status(self, task_id: int, status: str) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            task.status = status
            print(f"Task {task_id} status updated to '{status}'.")
   

    def set_prioritization(self, task_id: int, priority: str) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            task.priority = priority
            print(f"Task {task_id} priority updated to '{priority}'.")
  

    def set_new_date(self, task_id: int, deadline: datetime) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            task.deadline = deadline
            print(f"Task {task_id} deadline updated to {deadline}.")
    

    def mark_status_completed(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if task:
            task.status = "Completed"
            print(f"Task {task_id} marked as completed.")
            return True
        return False

    def get_task_by_id(self, task_id: int) -> Task:
        return self.task_management.get_task_by_id(task_id)