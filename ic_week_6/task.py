
from abc import ABC, abstractmethod
from datetime import datetime

class Task(ABC):
    def __init__(self, task_id, task_name, deadline):
        self._task_id = task_id
        self._task_name = task_name
        self._deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
        self._status = "Pending"
        self._priority = None
        self._color = None

    @property
    def task_id(self):
        return self._task_id

    @property
    def task_name(self):
        return self._task_name

    @property
    def deadline(self):
        return self._deadline

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def days_left(self):
        return (self._deadline - datetime.now().date()).days

    @abstractmethod
    def color_your_task(self):
        pass