from chief import Chief
from tasks import PersonalTask ,WorkTask

class TaskManagement(Chief):
    def __init__(self):
        self.ToDoList = []  

    def start_app(self):
        print("Gorev Yonetimi Baslatiliyor....")
        self.display_tasks()

    def add_task(self, task):
        try:
            self.ToDoList.append(task)
            print(f"Görev eklendi: {task.name}, ID: {task.id}")
        except Exception as e:
            print(f"Hata oluştu: {e}")

    def display_tasks(self):
        if not self.ToDoList:
            print("Görev listesi boş.")
        else:
            for task in self.ToDoList:
                print(task.display_task())
