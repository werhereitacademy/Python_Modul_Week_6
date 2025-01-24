# 1. Task (Soyut Sınıf)

from abc import ABC, abstractmethod
from datetime import datetime


class Task(ABC):
    def __init__(self, task_id: int, task_name: str, deadline: datetime, status: str = "Pending", priority: str = "Low"):
        self.task_id = task_id
        self.task_name = task_name
        self.deadline = deadline
        self.status = status
        self.priority = priority
        self.color = "Undefined"  # Varsayılan renk

    @abstractmethod
    def color_your_task(self) -> None:   # 	None dönüş türü, metot bir değer döndürmediğini belirtir.
        """Alt sınıflarda görev rengini ayarlamak için kullanılır."""
        pass

    def days_to_accomplish_task(self) -> int:
        """Görevin tamamlanmasına kalan gün sayısını döndürür."""
        today = datetime.now()
        remaining_days = (self.deadline - today).days
        return remaining_days

    def __str__(self):
        return f"""
        TASK ID   : {self.task_id}
        NAME      : {self.task_name}
        DEADLINE  : {self.deadline}
        STATUS    : {self.status}
        PRIORITY  : {self.priority}
        COLOR     : {self.color}
        """


# 2. PersonalTask (Task'tan Türetilen Sınıf)
class PersonalTask(Task):
    def __init__(self, task_id, task_name, deadline, status="Pending", priority="Low"):
        super().__init__(task_id, task_name, deadline, status, priority)
        self.color = "Blue"  # Özel rengi ayarla

    def color_your_task(self):
        return f"The task is marked with the color {self.color}"


# 3. WorkTask (Task'tan Türetilen Sınıf)
class WorkTask(Task):
    def __init__(self, task_id, task_name, deadline, status="Pending", priority="High"):
        super().__init__(task_id, task_name, deadline, status, priority)
        self.color = "Red"  # Özel rengi ayarla

    def color_your_task(self):
        return f"The task is marked with the color {self.color}"

