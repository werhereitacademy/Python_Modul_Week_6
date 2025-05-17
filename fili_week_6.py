# # TaskManagement Class:
# class TaskManagement:
#     def __init__(self):
#         self.taskList = []
#     def add_task(self, task):
#         self.taskList.append(task)
#     def display_tasks(self):
#         for task in self.taskList:
#             print(task.title) 

# # TaskScheduling Class:
# class TaskScheduling:
#     def __init__(self, task_manager):
#         self.task_manager = task_manager
#     def create_personal_task(self, title, deadline, priority):
#         task = PersonalTask(title, deadline, priority)
#         self.task_manager.add_task(task)
#     def create_work_task(self, title, deadline, project):
#         task = WorkTask(title, deadline, project)
#         self.task_manager.add_task(task)

# # TaskEditing Class:
# class TaskEditing:
#     def __init__(self, task_manager):
#         self.task_manager = task_manager
#     def edit_status(self, task_index, new_status):
#         if 0 <= task_index < len(self.task_manager.taskList):
#             self.task_manager.taskList[task_index].status = new_status
#     # Add methods for edit_priority, edit_deadline, search_task, remove_task


#     # Add: priority(self, i, p), deadline(self, i, d), find(self, query), remove(self, i)

# # TaskTracking Class:
# class TaskTracking:
#     def __init__(self, task_manager):
#         self.task_manager = task_manager
#     def get_status(self, task_index):
#         if 0 <= task_index < len(self.task_manager.taskList):
#             return self.task_manager.taskList[task_index].status
#         return "Task not found"
#     def mark_completed(self, task_index):
#         if 0 <= task_index < len(self.task_manager.taskList):
#             self.task_manager.taskList[task_index].status = "Completed"


# # Abstract Base Class (Task):
# from abc import ABC, abstractmethod

# class Task(ABC):
#     def __init__(self, title, deadline):
#         self.title = title
#         self.deadline = deadline
#         self.status = "Pending"

#     @abstractmethod
#     def display(self):
#         pass # Subclasses will implement how to display task details

# # PersonalTask and WorkTask Classes:
# class PersonalTask(Task):
#     def __init__(self, title, deadline, priority):
#         super().__init__(title, deadline)
#         self.priority = priority
#     def display(self):
#         print(f"Personal Task: {self.title}, Due: {self.deadline}, Priority: {self.priority}, Status: {self.status}")

# class WorkTask(Task):
#     def __init__(self, title, deadline, project):
#         super().__init__(title, deadline)
#         self.project = project
#     def display(self):
#         print(f"Work Task: {self.title}, Due: {self.deadline}, Project: {self.project}, Status: {self.status}")

# # SPECIAL_KEYWORDS Dictionary:

# SPECIAL_KEYWORDS = {
#     "today": ...,       # Implement logic to get today's date
#     "tomorrow": ...,    # Implement logic to get tomorrow's date
#     "next week": ...    # Implement logic to get next week's date
# }

# def process_deadline(deadline_input):
#     if deadline_input.lower() in SPECIAL_KEYWORDS:
#         return SPECIAL_KEYWORDS[deadline_input.lower()]
#     else:
#         return deadline_input 


from abc import ABC, abstractmethod

#  Existing Core 
class Task(ABC):
    def __init__(self, title, due_date): 
        self.title, self.due_date, self.status = title, due_date, "Pending"
    @abstractmethod
    def display(self): pass
class TaskManagement:
    def __init__(self): 
        self.tasks = []
    def add_task(self, task): 
        self.tasks.append(task)
    def display_tasks(self): 
        [t.display() for t in self.tasks]

# 1. StudyTask
class StudyTask(Task):
    def __init__(self, title, due_date, subject): 
        super().__init__(title, due_date); self.subject = subject; self.notes = ""
    def add_note(self, note): 
        self.notes += note
    def display(self): 
        print(f"Study: {self.title} (Due: {self.due_date}, Subj: {self.subject}, Notes: {self.notes}, Status: {self.status})")

# 2. Editing
class TaskEditor:
    def __init__(self, tm): 
        self.tasks = tm.tasks
    def color(self, i, c): 
        self.tasks[i].color = c if 0 <= i < len(self.tasks) else None
    def note(self, i, n): 
        self.tasks[i].notes = n if hasattr(self.tasks[i], 'notes') and 0 <= i < len(self.tasks) else None

# 3. Sorting
class TaskSorter:
    def __init__(self, tm): 
        self.tasks = tm.tasks
    def by_priority(self): 
        self.tasks.sort(key=lambda t: getattr(t, 'priority', float('inf')))
    def by_deadline(self): 
        self.tasks.sort(key=lambda t: t.due_date)

# 4. Simple Command-Line UI
class UI:
    def __init__(self, tm, te, ts): 
        self.tm, self.te, self.ts = tm, te, ts
    def create_study(self): 
        t = input("Title: "); d = input("Due: "); s = input("Subject: "); self.tm.add_task(StudyTask(t, d, s))
    def list(self): 
        self.tm.display_tasks()
    def edit_note(self): 
        i = int(input("Index: ")); n = input("Note: "); self.te.note(i, n)
    def sort_priority(self): 
        self.ts.by_priority()
    # ... more UI commands ...
    def run(self):
        while True:
            cmd = input("Command (create_study, list, edit_note, sort_prio, exit): ").lower()
            if cmd == "create_study": self.create_study()
            elif cmd == "list": self.list()
            elif cmd == "edit_note": self.edit_note()
            elif cmd == "sort_prio": self.sort_priority()
            elif cmd == "exit": break

# 5. Unit Tests (Conceptual - you'd use 'unittest' module)
def test_study_task_creation(): 
    assert StudyTask("Math", "2025-05-18", "Algebra").subject == "Algebra"
def test_add_note(): 
    task = StudyTask("Essay", "2025-05-20", "English"); task.add_note("Intro done"); assert task.notes == "Intro done"




