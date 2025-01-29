from task import  Task,PersonalTask,WorkTask

class TaskManagement:
    def __init__(self):
        self.task_list=[]
        self.next_id = 1
    def add_task(self,task_type, task_name, deadline, status, priority, color):
        if task_type == 'Personal':
            task = PersonalTask(self.next_id, task_name, deadline, status, priority, color)
        elif task_type == 'Work':
            task = WorkTask(self.next_id, task_name, deadline, status, priority, color)
        else:
            raise ValueError ('Gecersiz gorev turu.Personel veya Work gorev turunu seciniz.')
        self.task_list.append(task)
        self.next_id+=1
        

    def display_tasks(self):
        if not self.task_list:
            print('\nEklenmiş görev bulunmamaktadır.')
        else:
            print('\nMevcut Görevler:')
            for task in self.task_list:
                print(f'ID: {task.task_id} - {task.task_name} - Durum: {task.status} - Öncelik: {task.priority} = Renk: {task.color}' )






gorevYonetimi = TaskManagement()

# ✅ Kullanıcıdan Bilgi Alarak Görev Ekleme
print("\nYeni bir görev ekleyin:")
task_type = input("Görev Türü (Personal/Work): ").strip()
task_name = input("Görev İsmi: ").strip()
deadline = input("Son Tarih (YYYY-MM-DD): ").strip()
status = input("Durum (Pending/Completed): ").strip()
priority = input("Öncelik (High/Low): ").strip()
color = input("Renk (Blue/Red): ").strip()

# ✅ Görevi ekleyelim
print(gorevYonetimi.add_task(task_type, task_name, deadline, status, priority, color))

# ✅ Tüm görevleri listeleyelim
gorevYonetimi.display_tasks()