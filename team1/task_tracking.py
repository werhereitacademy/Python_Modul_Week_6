from task_management import*
from datetime import datetime, date
import json
import os

task_json = os.path.join(os.path.dirname(__file__), "tasks.json")

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

class TaskTracking:
    
    def __init__(self, task_management):
        self.task_file=file_upload()
        

    def get_task_status(self, task_id):
        task = next((t for t in self.task_management.task_list if t.task_id == task_id), None)
        if task:
            task.status
            file_save(self.task_list)
            return 

    def get_task_deadline(self, task_id):
        task = next((t for t in self.task_management.task_list if t.task_id == task_id), None)
        if task:
            task.deadline
            file_save(self.task_list)
            return 

    def get_task_color(self, task_id):
        task = next((t for t in self.task_management.task_list if t.task_id == task_id), None)
        if task:
            task.color
            file_save(self.task_list)
            return 