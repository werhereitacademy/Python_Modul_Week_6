# TaskManagement Class:
class TaskManagement:
    def __init__(self):
        self.taskList = []
    def add_task(self, task):
        self.taskList.append(task)
    def display_tasks(self):
        for task in self.taskList:
            print(task.title) 

# TaskScheduling Class:
class TaskScheduling:
    def __init__(self, task_manager):
        self.task_manager = task_manager
    def create_personal_task(self, title, deadline, priority):
        task = PersonalTask(title, deadline, priority)
        self.task_manager.add_task(task)
    def create_work_task(self, title, deadline, project):
        task = WorkTask(title, deadline, project)
        self.task_manager.add_task(task)

# TaskEditing Class:
class TaskEditing:
    def __init__(self, task_manager):
        self.task_manager = task_manager
    def edit_status(self, task_index, new_status):
        if 0 <= task_index < len(self.task_manager.taskList):
            self.task_manager.taskList[task_index].status = new_status
    # Add methods for edit_priority, edit_deadline, search_task, remove_task


    # Add: priority(self, i, p), deadline(self, i, d), find(self, query), remove(self, i)

# TaskTracking Class:
class TaskTracking:
    def __init__(self, task_manager):
        self.task_manager = task_manager
    def get_status(self, task_index):
        if 0 <= task_index < len(self.task_manager.taskList):
            return self.task_manager.taskList[task_index].status
        return "Task not found"
    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.task_manager.taskList):
            self.task_manager.taskList[task_index].status = "Completed"


# Abstract Base Class (Task):
from abc import ABC, abstractmethod

class Task(ABC):
    def __init__(self, title, deadline):
        self.title = title
        self.deadline = deadline
        self.status = "Pending"

    @abstractmethod
    def display(self):
        pass # Subclasses will implement how to display task details

# PersonalTask and WorkTask Classes:
class PersonalTask(Task):
    def __init__(self, title, deadline, priority):
        super().__init__(title, deadline)
        self.priority = priority
    def display(self):
        print(f"Personal Task: {self.title}, Due: {self.deadline}, Priority: {self.priority}, Status: {self.status}")

class WorkTask(Task):
    def __init__(self, title, deadline, project):
        super().__init__(title, deadline)
        self.project = project
    def display(self):
        print(f"Work Task: {self.title}, Due: {self.deadline}, Project: {self.project}, Status: {self.status}")

# SPECIAL_KEYWORDS Dictionary:

SPECIAL_KEYWORDS = {
    "today": ...,       # Implement logic to get today's date
    "tomorrow": ...,    # Implement logic to get tomorrow's date
    "next week": ...    # Implement logic to get next week's date
}

def process_deadline(deadline_input):
    if deadline_input.lower() in SPECIAL_KEYWORDS:
        return SPECIAL_KEYWORDS[deadline_input.lower()]
    else:
        return deadline_input 