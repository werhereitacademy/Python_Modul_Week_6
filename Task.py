from datetime import datetime, timedelta

class Task:
    taskList = []
    task_id = 0
    task_name = ""
    deadline = ""
    status = "pending"
    priority = ""
    color = ""

    def __init__(self, task_id, task_name, deadline, status, priority, color):
        self.task_id = task_id
        self.task_name = task_name
        self.deadline = deadline
        self.status = status
        self.priority = priority  # Fixed typo: 'priorty' to 'priority'
        self.color = color

    def colorTask(self, color):  # Added color as an argument
        self.color = color

    def days_to_accomplishTask(self, day):
        self.day = day  # consider renaming to self.days_remaining or similar for clarity


class TaskManagement:
    taskList = []

    def __init__(self):
        self.taskList = []

    def add_task(self, task):
        self.taskList.append(task)

    def display_tasks(self):
        print("\n " + "--------Task Details -------".center(100))
        # Corrected format string to match the number of arguments
        print(
            "\n{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15} ".format(
                "Task ID",
                "Task Name",
                "DeadLine",
                "COlor",
                "Status",
                "Priority",
                "Remaining Days",
            )
        )
        print("-" * 100)
        # for task in self.taskList:
        #   print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15} ".format(task.task_id,task.task_name,task.deadline,task.color,task.status,task.priority,task.renaming))
        # print("-" * 100)
        for task in self.taskList:
            try:
                print(
                    "{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15} ".format(
                        task.task_id,
                        task.task_name,
                        task.deadline,
                        task.color if hasattr(task, "color") else "",  # Check for 'color' attribute
                        task.status if hasattr(task, "status") else "",  # Check for 'status' attribute
                        task.priority if hasattr(task, "priority") else "",  # Check for 'priority' attribute
                        task.renaming if hasattr(task, "renaming") else "" , # Get 'renaming' attribute if it exists, otherwise use empty string
                    )
                )
            except AttributeError as e:
                print(f"Error displaying task: {e}")
        print("-" * 100)


class personelTask(Task):  # Inherit from Task to get the color attribute
    def __init__(self, task_id=None, task_name=None, deadline=None):  # Added parameters with default values
        super().__init__(task_id, task_name, deadline, "pending", "", "")
        # self.taskList = [] # Remove this line, it's already in TaskManagement
        # self.task_id = task_id # Remove this line, it's already handled in super().__init__
        # self.task_name = task_name # Remove this line, it's already handled in super().__init__
        # self.deadline = deadline # Remove this line, it's already handled in super().__init__

    def personelTask(self, task, priority):
        self.taskList.append(task)

    def colorTask(self, task):
        self.taskList.append(task)


class workTask(Task):  # Inherit from Task to get the color attribute
    def __init__(self, task_id=None, task_name=None, deadline=None):  # Added parameters
        super().__init__(task_id, task_name, deadline, "pending", "", "")
        # self.taskList = [] # Remove this line, it's already in TaskManagement
        # self.task_id = task_id # Remove this line, it's already handled in super().__init__
        # self.task_name = task_name # Remove this line, it's already handled in super().__init__
        # self.deadline = deadline # Remove this line, it's already handled in super().__init__

    def workTask(self, task):
        self.taskList.append(task)


class TaskEditting(TaskManagement):
    task_manage = TaskManagement()

    def __init__(self, task_manage):
        super().__init__()
        self.task_manage = task_manage

    def setTaskStatus(self, task_id, status):
        for task in self.task_manage.taskList:
            if task.task_id == task_id:
                task.status = status
                # self.task_manage.taskList[task_id].status = status

    def setTaskPriority(self, task_id, priority):
        self.task_manage.taskList[task_id].priority = priority  # This line may still cause an error

    def setTaskColor(self, task_id, color):
        self.task_manage.taskList[task_id].color = color  # This line may still cause an error
    #staticmethod
    def setNewDate(self, task_id, new_date):
        # self.task_manage.taskList[task_id].deadline = new_date  # This line may still cause an error
        for i in range(len(self.task_manage.taskList)):
            if self.task_manage.taskList[i].task_id == task_id:
                self.task_manage.taskList[i].deadline = new_date
                break

    def markStatus(self, task_id):
        self.task_manage.taskList[task_id].status = (
            "completed"  # This line may still cause an error
        )

    def getTaskById(self, task_id):
        return self.task_manage.taskList[task_id]


class TaskTracking(TaskManagement):
    task_manage = TaskManagement()

    def __init__(self, task_manage):
        super().__init__()
        self.task_manage = task_manage
        self.new_date = datetime.now()

    def taskStatus(self, task_id):
        return self.task_manage.taskList[task_id].status

    def taskDeadline(self, task_id):
        task = self.task_manage.taskList[task_id-1]
        deadline = datetime.strptime(task.deadline, "%Y-%m-%d")
        timenow = deadline - self.new_date
        task.renaming = timenow.days
        return timenow.days

    def colorTask(self, task_id):
        color = self.task_manage.taskList[task_id - 1].color
        return color

    def getTaskById(self, task_id):
        return self.task_manage.taskList[task_id - 1]


t1 = TaskManagement()
t = TaskEditting(t1)
tt = TaskTracking(t1)
p1 = personelTask(1, "p1", "2023-11-10")
w1 = workTask(2, "w1", "2025-6-10")
st1=workTask(3,"st1","2025-6-15")
t1.add_task(p1)
t1.add_task(w1)
t1.add_task(st1)
t1.display_tasks()
t.setTaskStatus(1, "in progress")
t1.display_tasks()
t.markStatus(1)  # This line may still cause an error
t1.display_tasks()
t.setTaskPriority(1, "not important")  # This line may still cause an error

t.setNewDate(2, "2025-06-15")
tt.taskDeadline(2)  # This line may still cause an error
t1.display_tasks()
t.setTaskColor(1, "red")
t1.display_tasks()
# tt.taskDeadline(2)  # This line may still cause an error
# tt.colorTask(2)
# t1.display_tasks()