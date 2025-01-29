#Module where the Task base class and the PersonnelTask ​​and WorkTask classes are defined
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import drawing, os

SPECIAL_KEYWORDS = {
    "today": datetime.now(),
    "tomorrow": datetime.now() + timedelta(days=1),
    "next week": datetime.now() + timedelta(weeks=1),
    "two weeks": datetime.now() + timedelta(weeks=2),
    "next month": datetime.now() + timedelta(days=30)
}

# Base abstract class for all tasks
class Task(ABC):
    task_field = ["Task ID", "Task Name", "Start Date", "Deadline", "Status", "Priority", "Color"]
    def __init__(self, task_id:int, name:str, deadline):
        self.__task_id = task_id
        self.__task_name = name
        self.__deadline = self.parse_deadline(deadline).strftime("%Y-%m-%d %H:%M:%S")
        self.__start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__status = "Pending"
        self.__priority = "Low"
        self.__color = ""

    def parse_deadline(self, deadline):
        # Parse the deadline string into a datetime object
        if isinstance(deadline, str):
            return SPECIAL_KEYWORDS.get(deadline.lower(), deadline)  
        elif isinstance(deadline, int):
            return datetime.now() + timedelta(days=deadline)
        elif isinstance(deadline, datetime):
            return deadline
        else:
            raise ValueError("Invalid deadline format")

    def set_task_id(self, task_id):
        self.__task_id = task_id
    def get_task_id(self):
        return self.__task_id
    
    def set_task_name(self, task_name):
        self.__task_name = task_name
    def get_task_name(self):
        return self.__task_name

    def set_deadline(self, deadline):
        self.__deadline = deadline.strftime("%Y-%m-%d %H:%M:%S")
    def get_deadline(self):
        return self.__deadline
    
    def set_start_date(self, start_date):
        self.__start_date = start_date.strftime("%Y-%m-%d %H:%M:%S")
    def get_start_date(self):
        return self.__start_date

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
    
    def get_task_dict(self):
        # ["Task ID", "Task Name", "Start Date", "Deadline", "Status", "Priority", "Color"]
        result = dict()
        result["Task ID"] = self.__task_id
        result["Task Name"] = self.__task_name
        result["Start Date"] = self.__start_date
        result["Deadline"] = self.__deadline
        result["Status"] = self.__status
        result["Priority"] = self.__priority
        result["Color"] = self.__color
        return result

    def display_info(self):
        for i,j in self.get_task_dict().items():
            print(f"{i}: {j}")

    def __str__(self):
        return f"Task ID: {self.__task_id}\nTask Name: {self.__task_name}\nDeadline: {self.__deadline}\nDescription: {self.__description}\nStart Date: {self.__start_date}\nStatus: {self.__status}\nPriority: {self.__priority}\nColor: {self.__color}"
    
    def days_to_accomplish(self):
        if self.__status == "Completed":
            return 0
        else:
            return (self.__deadline - datetime.now()).days
    
    @abstractmethod
    def color_your_task(self):
        self.__color = "Blue"

"""------------------------------------------------------------"""
# PersonnelTask class for tasks related to personnel
class PersonelTask(Task):
    def __init__(self, task_id, name, deadline):
        super().__init__(task_id, name, deadline)
        self.set_priority("Low")
        self.color_your_task()
    
    def color_your_task(self):
        self.set_color("Blue")
    
"""------------------------------------------------------------"""
# WorkTask class for tasks related to work
class WorkTask(Task):
    def __init__(self, task_id, name, deadline):
        super().__init__(task_id, name, deadline)
        self.set_priority("High")
        self.color_your_task()

    def color_your_task(self):
        self.set_color("Red")

"""------------------------------------------------------------"""
# ExamTask class for tasks related to work
class ExamTask(Task):
    def __init__(self, task_id, name, deadline):
        super().__init__(task_id, name, deadline)
        self.set_priority("Very High")
        self.color_your_task()

    def color_your_task(self):
        self.set_color("Green")

"""------------------------------------------------------------"""   
class TaskManagement:
    def __init__(self):
        self.__tasks = []

    def add_task(self, task):
        self.__tasks.append(task)
    
    def display_tasks(self):
        for task in self.__tasks:
            task.display_info()
            print("-"*40)

    def get_tasks(self):
        result = []
        for task in self.__tasks:
            result.append(task.get_task_dict())
        return result
    
    def get_fields(self):
        return Task.task_field
    
    def get_task_by_id(self, task_id):
        for task in self.task_list:
            if task.task_id == task_id:
                return task
        return None
    
"""------------------------------------------------------------"""
    
class TaskEditing:
    def __init__(self, task_management: TaskManagement):
        self.task_management = task_management

    def set_task_status(self, task_id, status):
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task.status = status

    def set_prioritization(self, task_id, priority):
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task.priority = priority

    def set_new_date(self, task_id, deadline):
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task.deadline = task.parse_deadline(deadline)

    def mark_status_completed(self, task_id):
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task.status = "Completed"
            return True
        return False

"""------------------------------------------------------------""" 

class TaskTracking:
    def __init__(self, task_management: TaskManagement):
        self.task_management = task_management

    def get_task_status(self, task_id):
        task = self.task_management.get_task_by_id(task_id)
        return task.status if task else None

    def get_task_deadline(self, task_id):
        task = self.task_management.get_task_by_id(task_id)
        return task.deadline if task else None

    def get_task_color(self, task_id):
        task = self.task_management.get_task_by_id(task_id)
        return task.color if task else None
    
"""------------------------------------------------------------"""


"""------------------------------------------------------------"""
class Chief:
    def __init__(self):
        self.task_management = TaskManagement()
        self.task_editing = TaskEditing(self.task_management)
        self.task_tracking = TaskTracking(self.task_management)
        self.main_menu = create_menu()
    def create_menu(self):
        return drawing.Menu(["Task Management System"], {
            "1": {"label": "Add Task", "action": self.add_task},
            "2": {"label": "Display Tasks", "action": self.task_management.display_tasks},
            "3": {"label": "Edit Task", "action": self.edit_task},
            "4": {"label": "Track Task", "action": self.track},
            "Q": {"label": "Quit / Exit E", "action": self.exit_program}
        })

    def create_personel_task(self):
        try:
            task_id = int(max(self.task_management.get_tasks(), key=lambda x: x["task_id"])["task_id"]) + 1
            task_name = input("Enter Task Name: ")
            deadline = input("Enter Deadline (e.g., today, tomorrow, next week, or YYYY-MM-DD): ")
            task = PersonelTask(task_id, task_name, deadline)
            self.task_management.add_task(task)
            print("Task added successfully!")
            input("Press Enter to continue...")
        except Exception as e:
            print("Error:", e)
            input("Press Enter to continue...")
    
    def create_work_task(self):
        try:
            task_id = int(max(self.task_management.get_tasks(), key=lambda x: x["task_id"])["task_id"]) + 1
            task_name = input("Enter Task Name: ")
            deadline = input("Enter Deadline (e.g., today, tomorrow, next week, or YYYY-MM-DD):")
            task = WorkTask(task_id, task_name, deadline)
            self.task_management.add_task(task)
            print("Task added successfully!")
            input("Press Enter to continue...")
        except Exception as e:
            print("Error:", e)
            input("Press Enter to continue...")
    
    def create_exam_task(self):
        try:
            task_id = int(max(self.task_management.get_tasks(), key=lambda x: x["task_id"])["task_id"]) + 1
            task_name = input("Enter Task Name: ")
            deadline = input("Enter Deadline (e.g., today, tomorrow, next week, or YYYY-MM-DD): ")
            task = ExamTask(task_id, task_name, deadline)
            self.task_management.add_task(task)
            print("Task added successfully!")
            input("Press Enter to continue...")
        except Exception as e:
            print("Error:", e)
            input("Press Enter to continue...")

    def add_task(self):
        task_id = int(max(self.task_management.get_tasks(), key=lambda x: x["task_id"])["task_id"]) + 1
        task_name = input("Enter Task Name: ")
        deadline = input("Enter Deadline (e.g., today, tomorrow, next week, or YYYY-MM-DD): ")
        task_type = input("Enter Task Type (Work/Exam/Pesonel): ").lower()
        if task_type == "exam":
            task = ExamTask(task_id, task_name, deadline)
        elif task_type == "work":
            task = WorkTask(task_id, task_name, deadline)
        else:
            PersonelTask(task_id, task_name, deadline)
        self.task_management.add_task(task)
        print("Task added successfully!")
        input("Press Enter to continue...")
    
    def edit_task(self):
        task_id = int(input("Enter Task ID to edit: "))
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task_editing = TaskEditing(self.task_management)
            task_editing.set_task_status(task_id, input("Enter New Status: "))
            task_editing.set_prioritization(task_id, input("Enter New Priority: "))
            task_editing.set_new_date(task_id, input("Enter New Deadline: "))
            print("Task edited successfully!")
        else:
            print("Task not found.")
        input("Press Enter to continue...")


    def main(self):
        self.main_menu.show()


"""------------------------------------------------------------"""

if __name__ == "__main__":
    task_manager = TaskManagement()
    task_manager.add_task(PersonelTask(1, "Task 1", datetime(2025, 2, 15)))
    task_manager.add_task(WorkTask(2, "Task 2", datetime(2025, 3, 15)))
    task_manager.add_task(ExamTask(3,"Task 3","Next Week"))
    task_manager.add_task(ExamTask(4,"Task 4",5))
    grid = drawing.create_grid(task_manager.get_tasks(), task_manager.get_fields(),[8, 15, 19, 19, 10, 10, 10],"Task Management")
    for i in grid:
        print(i)

    # chief = Chief()
    # chief.main()
    