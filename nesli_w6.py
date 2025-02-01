class PersonelTask(Task):
    def __init__(self,task_id,task_name, deadline):
        super().__init__(self, task_id,task_name,deadline)
        self.set_priority("Low")
        self.color_your_task()
    
    def color_your_task(self):
        self.set_color("Blue")
    
class TaskEditing:
    def __init__(self, task_management):
        self.task_management = task_management #referans
        #task_management nesnesini aldik ve sakladik
    
    def set_task_status(self, task_id, status):
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task.set_status(status)
            print(f"Gorev {task_id} durumu '{status}' olarak guncellendi.")
        else:
            raise Exception("task bulunamadi")#hata urettik #try exception da kullanilabilir.

    def set_prioritization(self, task_id, priority):
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task.set_priority(priority)
            print(f"Gorev {task_id} onceligi '{priority} olarak degistirildi")
        else:
            raise Exception("task bulunamadi")
    
    def set_new_date(self, task_id, deadline):
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task.set_deadline(deadline)
            print(f"Gorev {task_id} yeni teslim tarihi: '{deadline} olarak degistirildi")
        else:
            raise Exception("task bulunamadi")

    def mark_status_completed(self, task_id):
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task.set_status("completed")
            print(f"Gorev {task_id} tamamlandi!")
        else:
            raise Exception("task bulunamadi")
