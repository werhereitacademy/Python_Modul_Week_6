from task_management import TaskManagement

class TaskEditing:
    def __init__(self, task_management):
        self.task_management = task_management

    def edit_task(self, id, new_type=None, new_name=None, new_priority=None, new_due_date=None):
        try:
            for task in self.task_management.ToDoList:
                if task.id == id:
                    if new_type:
                        task.type = new_type
                    if new_name:
                        task.name = new_name
                    if new_priority:
                        task.priority = new_priority
                    if new_due_date:
                        task.due_date = new_due_date
                    print(f"Görev '{id}' güncellendi.")
                    return
            print(f"Görev '{id}' bulunamadı.")
        except Exception as e:
            print(f"Hata oluştu: {e}")