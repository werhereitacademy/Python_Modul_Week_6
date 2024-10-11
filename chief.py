from abc import ABC, abstractmethod


class Chief(ABC):
    @abstractmethod
    def start_app(self):
        pass

    @abstractmethod
    def add_task(self, task):
        pass

    @abstractmethod
    def display_tasks(self):
        pass