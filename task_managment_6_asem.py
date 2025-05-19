class TaskManagement:
    def __init__(self ,taskList):
        self.taskList=taskList
        self.task_id_counter = 1

    
    def add_task(self,task):
        task.id = self.task_id_counter
        self.taskList.append(task)
        self.task_id_counter += 1

    

    def display_task(self):
         for task in self.taskList:
            task.display()
    
    def sort_tasks(self, by="priority"):
         if by == "priority":
              self.taskList.sort(key=lambda task: task.priority.lower())
              print("Tasks sorted by priority.")
         elif by == "deadline":
              self.taskList.sort(key=lambda task: task.due_date)
              print("Tasks sorted by deadline.")
         else:
              print("Invalid sort option. Use 'priority' or 'deadline'.")





tm=TaskManagement([])
tm.display_task()

class TaskScheduling:
    def __init__(self,task_manager):
        self.task_manager=task_manager
    
    def create_and_add_task(self, task_type, title, description, due_date):
            if task_type == "personal":
                         task = PersonalTask(title, description, due_date)
            elif task_type == "work":
                  task = WorkTask(title, description, due_date)
            else:
                  print("Invalid task type. Please use 'personal' or 'work'.")
                  return
            self.task_manager.add_task(task)

from abc import ABC, abstractmethod

class Priorization(ABC):
    @abstractmethod
    def set_priority(self, priority):
        pass


class Task(ABC):
      @abstractmethod
      def __init__(self, title, description, due_date):
            pass
      
      @abstractmethod
      def display(self):
        pass
from datetime import datetime, timedelta

SPECIAL_KEYWORDS = {
    "today": datetime.today().date(),
    "tomorrow": (datetime.today() + timedelta(days=1)).date(),
    "next week": (datetime.today() + timedelta(days=7)).date()
}


class PersonalTask(Task,Priorization):
      def __init__(self,title,description,due_date,category="General"):
            self.id = None
            self.title=title
            self.description=description
            self.due_date=due_date
            self.status = "Pending"
            self.priority = "Normal"
            self.category = category
            self.color = "None"
            self.notes = ""
      
      def display(self):
           remaining_days = (self.due_date - datetime.today().date()).days
           print(f"Task ID: {self.id}, Name: {self.title}, Deadline: {self.due_date}, "
              f"Color: {self.color}, Status: {self.status}, "
              f"Priority: {self.priority}, Remaining Days: {remaining_days}")

      def set_priority(self, priority):
        self.priority = priority

        

class WorkTask(Task,Priorization):
      def __init__(self,title,task_id,description,due_date,department="General"):
            self.id = task_id
            self.title=title
            self.description=description
            self.due_date=due_date
            self.status = "Pending"
            self.priority = "Normal"
            self.department = department
            self.color = "None"
            self.notes = ""

        
      def display(self):
            remaining_days = (self.due_date - datetime.today().date()).days
            print(f"Task ID: {self.id}, Name: {self.title}, Deadline: {self.due_date}, "
              f"Color: {self.color}, Status: {self.status}, "
              f"Priority: {self.priority}, Remaining Days: {remaining_days}")
     
      def set_priority(self, priority):
        self.priority = priority

class TaskEditing:
      
      def edit_title(self,task,new_title):
            task.title = new_title
      
      def edit_description(self,task,new_description):
            task.description = new_description
       
      def edit_due_date(self,task,new_due_date):
            task.due_date = new_due_date
      
      def  edit_status(self,task,new_status):
            task.status = new_status
       
      def edit_priority (self,task,new_priority):
            task.priority=new_priority
      
      def search_task(self,task_list,search_title):
            for task in task_list:
                  if task.title == search_title:
                        print(task)
            
      def remove_task(self,task_list,task_remove):
            for task in task_list:
                  if task.title == task_remove:
                        task_list.remove(task)
                        break
      def edit_color(self, task, new_color):
             task.color = new_color

      def add_note(self, task, note_text):
            task.notes += f"\n- {note_text}"

class TaskTracking:
      
      def track_task_status(self,task):
            print(task.status)
      
      def task_as_completed(self, task):
            task.status = "Completed"


class StudyTask(Task, Priorization):
    def __init__(self, title, description, due_date, subject, study_duration):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Pending"
        self.priority = "Normal"
        self.subject = subject               
        self.study_duration = study_duration  
        self.color = "None"
        self.notes = ""

    def display(self):
          remaining_days = (self.due_date - datetime.today().date()).days
          print(f"Task ID: {self.id}, Name: {self.title}, Deadline: {self.due_date}, "
              f"Color: {self.color}, Status: {self.status}, "
              f"Priority: {self.priority}, Remaining Days: {remaining_days}")

    def set_priority(self, priority):
        self.priority = priority



def main():
    task_manager = TaskManagement([])
    scheduler = TaskScheduling(task_manager)
    editor = TaskEditing()
    tracker = TaskTracking()

    while True:
        print("\nTask Management Menu:")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Edit Task")
        print("4. Mark Task as Completed")
        print("5. Sort Tasks")
        print("6. Exit")

        choice = input("Select an option (1–6): ")

        if choice == "1":
            task_type = input("Enter task type (personal/work/study): ").lower()
            title = input("Title: ")
            description = input("Description: ")
            due = input("Due date (today, tomorrow, next week or YYYY-MM-DD): ").lower()

            if due in SPECIAL_KEYWORDS:
                due_date = SPECIAL_KEYWORDS[due]
            else:
                due_date = datetime.strptime(due, "%Y-%m-%d").date()

            if task_type == "study":
                subject = input("Subject: ")
                duration = input("Study Duration: ")
                task = StudyTask(title, description, due_date, subject, duration)
                task_manager.add_task(task)
            else:
                scheduler.create_and_add_task(task_type, title, description, due_date)

        elif choice == "2":
            for task in task_manager.taskList:
                task.display()
                print("-" * 30)

        elif choice == "3":
            title = input("Enter title of the task to edit: ")
            for task in task_manager.taskList:
                if task.title == title:
                    field = input("What would you like to edit? (title/description/due_date/status/priority/color/note): ").lower()
                    if field == "title":
                        editor.edit_title(task, input("New title: "))
                    elif field == "description":
                        editor.edit_description(task, input("New description: "))
                    elif field == "due_date":
                        new_date = input("New due date (YYYY-MM-DD): ")
                        editor.edit_due_date(task, datetime.strptime(new_date, "%Y-%m-%d").date())
                    elif field == "status":
                        editor.edit_status(task, input("New status: "))
                    elif field == "priority":
                        editor.edit_priority(task, input("New priority: "))
                    elif field == "color":
                        editor.edit_color(task, input("New color: "))
                    elif field == "note":
                        editor.add_note(task, input("Note to add: "))
                    print("Task updated.")
                    break
            else:
                print("Task not found.")

        elif choice == "4":
            title = input("Enter title of the task to mark as completed: ")
            for task in task_manager.taskList:
                if task.title == title:
                    tracker.task_as_completed(task)
                    print("Task marked as completed.")
                    break
            else:
                print("Task not found.")

        elif choice == "5":
            sort_by = input("Sort by 'priority' or 'deadline'? ")
            task_manager.sort_tasks(sort_by)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()
