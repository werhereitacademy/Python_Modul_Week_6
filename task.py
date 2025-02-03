#Module where the Task base class and the PersonnelTask ​​and WorkTask classes are defined
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import drawing, os
import file_transactions as ft

SPECIAL_KEYWORDS = {
    "today": datetime.now(),
    "tomorrow": datetime.now() + timedelta(days=1),
    "next week": datetime.now() + timedelta(weeks=1),
    "two weeks": datetime.now() + timedelta(weeks=2),
    "next month": datetime.now() + timedelta(days=30)
}

# Base abstract class for all tasks
class Task(ABC):
    task_id = 0
    task_field = ["Task ID", "Task Name", "Start Date", "Deadline", "Status", "Priority", "Color","Remaining Days"]
    file_name = "task.txt"
    def __init__(self, task_id:int, name:str, deadline):
        self.__task_id = task_id
        self.__task_name = name
        self.__deadline = self.parse_deadline(deadline)
        self.__start_date = datetime.now()
        self.__status = "Pending"
        self.__priority = "Low"
        self.__color = ""
        Task.task_id += 1

    def parse_deadline(self, deadline):
        # Parse the deadline string into a datetime object
        if isinstance(deadline, str) and deadline.lower() in SPECIAL_KEYWORDS.keys():
            return SPECIAL_KEYWORDS.get(deadline.lower(), deadline)  
        elif deadline.isdigit():
            return datetime.now() + timedelta(days=int(deadline))
        elif isinstance(deadline, datetime):
            return deadline
        elif isinstance(deadline, str):
            if len(deadline) > 10:
                return datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S")
            else:
                return datetime.strptime(deadline, "%Y-%m-%d")
        else:
            # raise ValueError("Invalid deadline format")
            return datetime.now()+timedelta(days=7)
            pass
           

    def set_task_id(self, task_id):
        self.__task_id = task_id
    def get_task_id(self):
        return self.__task_id
    
    def set_task_name(self, task_name):
        self.__task_name = task_name
    def get_task_name(self):
        return self.__task_name

    def set_deadline(self, deadline):
        self.__deadline = self.parse_deadline(deadline)
    def get_deadline(self):
        return self.__deadline
    
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
        # ["Task ID", "Task Name", "Start Date", "Deadline", "Status", "Priority", "Color", "Remaining Days"]
        result = dict()
        result["Task ID"] = self.__task_id
        result["Task Name"] = self.__task_name
        result["Start Date"] = self.__start_date.strftime("%Y-%m-%d %H:%M:%S")
        result["Deadline"] = self.__deadline.strftime("%Y-%m-%d %H:%M:%S")
        result["Status"] = self.__status
        result["Priority"] = self.__priority
        result["Color"] = self.__color
        result["Remaining Days"] = self.days_to_accomplish()
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
# StudyTask class for tasks related to work
class StudyTask(Task):
    def __init__(self, task_id, name, deadline):
        super().__init__(task_id, name, deadline)
        self.set_priority("Very High")
        self.color_your_task()

    def color_your_task(self):
        self.set_color("Bordo")
"""------------------------------------------------------------"""
# SocialTask class for tasks related to social
class SocialTask(Task):
    def __init__(self, task_id, name, deadline):
        super().__init__(task_id, name, deadline)
        self.set_priority("medium")
        self.color_your_task()

    def color_your_task(self):
        self.set_color("Green")


"""------------------------------------------------------------"""   
class TaskManagement:
    def __init__(self):
        self.__tasks = []
        if os.path.exists(Task.file_name):
            load_tasks = ft.load_file(Task.file_name)
            max_id = 0
            for i in load_tasks:
                if i["Color"]== "Blue":
                    task = PersonelTask(i["Task ID"], i["Task Name"], i["Deadline"])
                    self.add_task(task)
                elif i["Color"]== "Red":
                    task = WorkTask(i["Task ID"], i["Task Name"], i["Deadline"])
                    self.add_task(task)
                elif i["Color"]== "Bordo":
                    task= StudyTask(i["Task ID"], i["Task Name"], i["Deadline"])
                    self.add_task(task)
                elif i["Color"]== "Green":
                    task=SocialTask(i["Task ID"], i["Task Name"], i["Deadline"])
                    self.add_task(task)
                if i["Task ID"] > max_id:
                    max_id = i["Task ID"]
            Task.task_id = max_id                
        

    def add_task(self, task):
        self.__tasks.append(task)
        ft.save_file(Task.file_name, self.get_tasks())
    
    def remove_task(self, task_id):
        for task in self.__tasks:
            if task.get_task_id() == task_id:
                self.__tasks.remove(task)
                ft.save_file(Task.file_name, self.get_tasks())
                return True
        return False
    
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
        for task in self.__tasks:
            if task.get_task_id() == task_id:
                return task
        return None
    
"""------------------------------------------------------------"""
    
class TaskEditing:
    def __init__(self, task_management: TaskManagement):
        self.task_management = task_management

    def set_task_status(self, task_id, status):
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task.set_status(status)

    def set_prioritization(self, task_id, priority):
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task.set_priority(priority)

    def set_new_date(self, task_id, deadline):
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task.set_deadline(deadline)

    def mark_status_completed(self, task_id):
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task.set_status("Completed")
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
        self.menu = []
        self.menu.append(["╔═══════════════════════════════════════════════════════════╗ ",
        "║             WELCOME TO TASK MANAGEMENT SYSTEM             ║ ",
        "╠═══════════════════════════════════════════════════════════╣ ",
        "║                                                           ║ ",
        "║                (1) Add Task                               ║ ",
        "║                (2) Update Task                            ║ ",
        "║                (3) Task Completed                         ║ ",
        "║                (4) Delete a Task                          ║ ",
        "║                (5) Search Task                            ║ ",
        "║                                                           ║ ",
        "╠═══════════════════════════════════════════════════════════╣ ",
        "║                    (Q) Quit / Exit                        ║ ",
        "╚═══════════════════════════════════════════════════════════╝ "])
        self.menu.append(["╔═══════════════════════════════════════════════════════════╗ ",
        "║             WELCOME TO TASK MANAGEMENT SYSTEM             ║ ",
        "╠═══════════════════════════════════════════════════════════╣ ",
        "║                                                           ║ ",
        "║                (1) Add Personal Task                      ║ ",
        "║                (2) Add Work Task                          ║ ",
        "║                (3) Add Study Task                         ║ ",
        "║                (4) Add Social Task                        ║ ",
        "║                                                           ║ ",
        "╠═══════════════════════════════════════════════════════════╣ ",
        "║                  (Q) Quit Add Task Menu                   ║ ",
        "╚═══════════════════════════════════════════════════════════╝ "])
        
        
        


    def create_personel_task(self):
        try:
            task_id = Task.task_id + 1
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
            task_id = Task.task_id + 1
            task_name = input("Enter Task Name: ")
            deadline = input("Enter Deadline (e.g., today, tomorrow, next week, or YYYY-MM-DD):")
            task = WorkTask(task_id, task_name, deadline)
            self.task_management.add_task(task)
            print("Task added successfully!")
            input("Press Enter to continue...")
        except Exception as e:
            print("Error:", e)
            input("Press Enter to continue...")
    
    def create_study_task(self):
        try:
            task_id = Task.task_id + 1
            task_name = input("Enter Task Name: ")
            deadline = input("Enter Deadline (e.g., today, tomorrow, next week, or YYYY-MM-DD): ")
            task = StudyTask(task_id, task_name, deadline)
            self.task_management.add_task(task)
            print("Task added successfully!")
            input("Press Enter to continue...")
        except Exception as e:
            print("Error:", e)
            input("Press Enter to continue...")
    
    def create_social_task(self):
        try:
            task_id = Task.task_id + 1
            task_name = input("Enter Task Name: ")
            deadline = input("Enter Deadline (e.g., today, tomorrow, next week, or YYYY-MM-DD): ")
            task = SocialTask(task_id, task_name, deadline)
            self.task_management.add_task(task)
            print("Task added successfully!")
            input("Press Enter to continue...")
        except Exception as e:
            print("Error:", e)
            input("Press Enter to continue...")
    
    def edit_task(self, task_id):
        try:
            task = self.task_management.get_task_by_id(task_id)
            if task:
                task_editing = TaskEditing(self.task_management)
                task_editing.set_task_status(task_id, input("Enter New Status: "))
                task_editing.set_prioritization(task_id, input("Enter New Priority: "))
                task_editing.set_new_date(task_id, input("Enter New Deadline(e.g., today, tomorrow, next week, or YYYY-MM-DD): "))
                print("Task edited successfully!")
            else:
                print("Task not found.")
            input("Press Enter to continue...")
        except Exception as e:
            print("Error:", e)
            input("Press Enter to continue...")

    def track(self):
        task_id = int(input("Enter Task ID to track: "))
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task_tracking = TaskTracking(self.task_management)
            task_tracking.get_task_status(task_id)
            task_tracking.get_task_prioritization(task_id)
            task_tracking.get_task_date(task_id)

    def delete_task(self):
        try:
            task_id = int(input("Enter Task ID to delete: "))
            self.task_management.delete_task(task_id)
            print("Task deleted successfully!")
            input("Press Enter to continue...")
        except Exception as e:
            print("Error:", e)
            input("Press Enter to continue...")
    def search_order(self):
        try:
            search_task = {}
            order_field = {}
            run_menu = True
            invalid_input = False
            while run_menu:
                os.system("cls" if os.name == "nt" else "clear")
                print("╔═══════════════════════════════════════════════════════════╗ ")
                print("║                  Search Task Criteria:                    ║ ")
                for i in search_task:
                    p_str = i +" "+ str(search_task[i][0])+" "+str(search_task[i][1])
                    print("║    "+p_str+ (" " * (55-len(p_str)))+"║")
                print("╠═══════════════════════════════════════════════════════════╣ ")
                print("║    Equal(1)/In(11)    Search by Task Name                 ║ ")
                print("║    Equal(2)/In(12)    Search by Task Status               ║ ")
                print("║    Equal(3)/In(13)    Search by Task Prioritization       ║ ")
                print("║    Equal(4)/less(14)  Search by Task Remaining Days       ║ ")
                print("║    Equal(5)/In(15)    Search by Task Color                ║ ")
                print("╠═══════════════════════════════════════════════════════════╣")
                print("║                   Order Task Criteria:                    ║")
                for i in order_field:
                    p_str = i +" "+ order_field[i]
                    print("║    "+p_str+ (" " * (55-len(p_str)))+"║")
                print("╠═══════════════════════════════════════════════════════════╣")
                print("║    Asc(6)/Desc(16)    Search by Task Name                 ║")
                print("║    Asc(7)/Desc(17)    Search by Task Status               ║")
                print("║    Asc(8)/Desc(18)    Search by Task Priority             ║")
                print("║    Asc(9)/Desc(19)    Search by Task Remaining Days       ║")
                print("║    Asc(10)/Desc(20)   Search by Task Color                ║")
                print("╠═══════════════════════════════════════════════════════════╣")
                print("║           (Q) Quit Search and Order Menu                  ║")
                print("╚═══════════════════════════════════════════════════════════╝")
                if invalid_input:
                    print("Invalid input. Please try again.")
                    invalid_input = False
                choice = input("Please choose an option: ")
                if choice.lower() in["q","quit","e","exit"]:
                    run_menu = False
                elif choice == "1":
                    search_task["Task Name"] = ["=",input("Enter Task Name: ")]
                elif choice == "2":
                    search_task["Status"] = ["=",input("Enter Task Status: ")]
                elif choice == "3":
                    search_task["Priority"] = ["=",input("Enter Task Priority: ")]
                elif choice == "4":
                    search_task["Remaining Days"] = ["=",input("Enter Task Date: ")]
                elif choice == "5":
                    search_task["Color"] = ["=",input("Enter Task Color: ")]
                elif choice == "11":
                    search_task["Task Name"] = ["In",input("Enter Task Name: ")]
                elif choice == "12":
                    search_task["Status"] = ["In",input("Enter Task Status: ")]
                elif choice == "13":
                    search_task["Priority"] = ["In",input("Enter Task Priority: ")]
                elif choice == "14":
                    search_task["Remaining Days"] = ["less",input("Enter Task Date: ")]
                elif choice == "15":
                    search_task["Color"] = ["In",input("Enter Task Color: ")]
                elif choice == "6":
                    order_field["Task Name"] = "Asc"
                elif choice == "7":
                    order_field["Status"] = "Asc"
                elif choice == "8":
                    order_field["Priority"] = "Asc"
                elif choice == "9":
                    order_field["Remaining Days"] = "Asc"
                elif choice == "10":
                    order_field["Color"] = "Asc"
                elif choice == "16":
                    order_field["Task Name"] = "Desc"
                elif choice == "17":
                    order_field["Status"] = "Desc"
                elif choice == "18":
                        order_field["Priority"] = "Desc"
                elif choice == "19":
                    order_field["Remaining Days"] = "Desc"
                elif choice == "20":
                    order_field["Color"] = "Desc"
                else:
                    invalid_input = True
            self.display_search_result(search_task, order_field)
        except Exception as e:
            print("Error: ", e)
            input("Press any key to continue...")

    def display_search_result(self, search_task, order_field):
        search_tasks = []
        for task in self.task_management.get_tasks():
            addtask = True
            for key in search_task: 
                if search_task[key][0] == "=":
                    if task[key] != search_task[key][1]:
                        addtask = False
                elif search_task[key][0] == "In":
                    if search_task[key][1] not in task[key]:
                        addtask = False
                elif search_task[key][0] == "less":
                    if task[key] < search_task[key][1]:
                        addtask = False
            if addtask:
                search_tasks.append(task)
            if order_field:
                search_tasks = sorted(search_tasks, key=lambda x: x[list(order_field.keys())[0]], reverse=order_field[list(order_field.keys())[0]] == "Desc")

        self.display_grid(search_tasks, ["Task ID", "Task Name", "Deadline", "Status", "Priority", "Color","Remaining Days"],[8, 15, 19, 10, 10, 10, 14],"Task List")
        input("Press Enter to continue...")
            
    def display_menu(self, menu=0, invalid_choice=False):
        try:
            os.system("cls" if os.name == "nt" else "clear")
            self.display_grid(self.task_management.get_tasks(), ["Task ID", "Task Name", "Deadline", "Status", "Priority", "Color","Remaining Days"],[8, 15, 19, 10, 10, 10, 14],"Task List")
            for line in self.menu[menu]:
                print(line)
            if invalid_choice:
                print("Invalid choice. Please try again.")
            return input("Please choose an option: ")
        except Exception as e:
            print("Error:", e)
            input("Press Enter to continue...")
            return "Q"
    def task_add_menu(self):
        add_task_menu = True
        refunction = False
        while add_task_menu:
            choise = self.display_menu(menu=1, invalid_choice=refunction)
            if choise.lower() in ["e", "q", "quit", "exit"]:
                add_task_menu = False
            elif choise == "1":
                try:
                    self.create_personel_task()
                except Exception as e:
                    print("Error:", e)
                    input("Press Enter to continue...")
                
            elif choise == "2":
                try:
                    self.create_work_task()
                except Exception as e:
                    print("Error:", e)
                    input("Press Enter to continue...")
                
            elif choise == "3":
                try:
                    self.create_study_task()
                except Exception as e:
                    print("Error:", e)
                    input("Press Enter to continue...")
            
            elif choise == "4":
                try:
                    self.create_social_task()
                except Exception as e:
                    print("Error:", e)
                    input("Press Enter to continue...")
            else:
                refunction = True
    def display_grid(self, tasks, fields, sizes, title):
        try:
            grid = drawing.create_grid(tasks, fields, sizes, title)
            for i in grid:
                print(i)
        except Exception as e:
            print("Grid not Show, Error:", e)
            input("Press Enter to continue...")
    def main(self):
        run_program = True
        invalid_choice = False
        while run_program:
            choise = self.display_menu(invalid_choice=invalid_choice)
            if choise.lower() in ["e", "q", "quit", "exit"]:
                run_program = False
                print("Exiting the program...")
                input("Press Enter to continue...")
            elif choise == "1":
                try:
                    self.task_add_menu()
                except Exception as e:
                    print("Error:", e)
                    input("Press Enter to continue...")
            elif choise == "2":
                try:
                    taskid= input("Enter Task ID to edit: ")
                    while taskid.isnumeric() == False:
                        print("Invalid input. Please enter a valid Task ID.")
                        taskid= input("Enter Task ID to edit: ")
                    self.edit_task(int(taskid))
                except Exception as e:
                    print("Error:", e)
                    input("Press Enter to continue...")    
            elif choise == "3":
                try:
                    taskid= input("Enter Task ID to mark as completed: ")
                    while taskid.isnumeric() == False:
                        print("Invalid input. Please enter a valid Task ID.")
                        taskid= input("Enter Task ID to mark as completed: ")
                    self.task_editing.mark_status_completed(int(taskid))
                except Exception as e:
                    print("Error:", e)
                    input("Press Enter to continue...")
            elif choise == "4":
                try:
                    taskid= input("Enter Task ID to delete: ")
                    while taskid.isnumeric() == False:
                        print("Invalid input. Please enter a valid Task ID.")
                        taskid= input("Enter Task ID to delete: ")
                    self.task_management.remove_task(int(taskid))
                except Exception as e:
                    print("Error:", e)
                    input("Press Enter to continue...")
            elif choise == "5": 
                try:
                    self.search_order()
                except Exception as e:
                    print("Error:", e)
                    input("Press Enter to continue...")
            else:
                invalid_choice = True

"""------------------------------------------------------------"""

if __name__ == "__main__":
    # task_manager = TaskManagement()
    # task_manager.add_task(PersonelTask(1, "Task 1", datetime(2025, 2, 15)))
    # task_manager.add_task(WorkTask(2, "Task 2", datetime(2025, 3, 15)))
    # task_manager.add_task(StudyTask(3,"Task 3","Next Week"))
    # task_manager.add_task(SocialTask(4,"Task 4",12))

    # grid = drawing.create_grid(task_manager.get_tasks(), task_manager.get_fields(),[8, 15, 19, 19, 10, 10, 10,14],"Task Management")
    # for i in grid:
    #     print(i)

    chief = Chief()
    chief.main()
    