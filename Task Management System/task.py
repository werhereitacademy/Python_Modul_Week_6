from abc import ABC, abstractmethod
from datetime import datetime

class Task(ABC):
    pass


class PersonalTask(Task):
    pass

class WorkTask(Task):
    pass