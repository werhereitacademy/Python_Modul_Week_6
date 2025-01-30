from task import PersonalTask, WorkTask
from datetime import datetime
import json

task_json = "tasks.json"

def file_upload():
    try:
        with open(task_json, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        print("Dosya bulunamadi veya JSON hatali! Yeni bir dosya olusturuluyor.")
        return []

def file_save(data):
    with open(task_json, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

class TaskManagement:
    def __init__(self):
        self.task_list = file_upload()
        task_ids = [task["task_id"] for task in self.task_list]
        self.next_id = max(task_ids, default=0) + 1

    def add_task(self, task_type, task_name, deadline):
        try:
            deadline = datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            print("Hatalı tarih formatı! YYYY-MM-DD şeklinde giriniz.")
            return

        if task_type == "Personal":
            task = PersonalTask(self.next_id, task_name, deadline)
        elif task_type == "Work":
            task = WorkTask(self.next_id, task_name, deadline)
        else:
            raise ValueError("Geçersiz görev türü. 'Personal' veya 'Work' seçiniz.")

        self.next_id += 1

        task_dict = {
            "task_id": task.task_id,
            "task_name": task.task_name,
            "deadline": task.deadline.strftime("%Y-%m-%d"),
            "status": task.status,
            "priority": task.priority,
            "color": task.color
        }

        self.task_list.append(task_dict)
        file_save(self.task_list)

    def display_tasks(self):
        if not self.task_list:
            print("\nEklenmiş görev bulunmamaktadır.")
        else:
            print("\nMevcut Görevler:")
            for task in self.task_list:
                print(f'ID: {task["task_id"]} - {task["task_name"]} - Durum: {task["status"]} - Öncelik: {task["priority"]} - Renk: {task["color"]}')

gorevYonetimi = TaskManagement()
print("\nYeni bir görev ekleyin:")
task_type = input("Görev Türü (Personal/Work): ").strip()
task_name = input("Görev İsmi: ").strip()
deadline = input("Son Tarih (YYYY-MM-DD): ").strip()

gorevYonetimi.add_task(task_type, task_name, deadline)
gorevYonetimi.display_tasks()