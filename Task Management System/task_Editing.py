#tüm görevleri içeren bir task_list olusturacaz
#hangi gorevleri duzenleyecgimiz bilcez
class TaskEditing:
    def __init__(self, task_list):
        self.task_list = task_list
#id verilen gorevi bulacaz
    def find_task(self, task_id):
        for task in self.task_list:
            if task.task_id == task_id:
                return task
        raise ValueError("Görev bulunamadi")
#gorevin yapilip yapilmadigini durumun aciklayacz
    def update_status(self, task_id, new_status):
    task = self.find_task(task_id)
    task.status = new_status
    print(f"{task.task_name} adli görevin durumu '{new_status}' olarak güncellendi.")
