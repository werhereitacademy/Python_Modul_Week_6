class TaskTracking:
    def __init__(self, task_management):
        self.task_management = task_management

    def mark_task_complete(self, id):
        try:
            for task in self.task_management.ToDoList:
                if task.id == id:
                    task.mark_as_complete()
                    print(f"Görev '{id}' tamamlandı olarak işaretlendi.")
                    return
            print(f"Görev '{id}' bulunamadı.")
        except Exception as e:
            print(f"Hata oluştu: {e}")
            