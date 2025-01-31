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
    
    def __init__(self):
        self.task_list = file_upload()

    def get_task_status(self, task_id):
        task = next((t for t in self.task_list if t["task_id"] == task_id), None)  # task_id'yi kullanmalıyız
        if task:
            return task["status"]  # Durum değerini döndür
        else:
            print(f"Görev ID {task_id} bulunamadı!")
            return None

    def get_task_deadline(self, task_id):
        task = next((t for t in self.task_list if t["task_id"] == task_id), None)  # task_id'yi kullanmalıyız
        if task:
            return task["deadline"]  # Deadline değerini döndür
        else:
            print(f"Görev ID {task_id} bulunamadı!")
            return None

    def get_task_color(self, task_id):
        task = None  # Başlangıçta görev bulunmadı olarak ayarla

        for t in self.task_list:  # Listeyi sırayla gez
            if t["task_id"] == task_id:  # Eğer task_id eşleşiyorsa
                task = t  # Görevi bul ve task değişkenine ata
                break  # Döngüyü sonlandır
          
        if task is not None:# Eğer task bulunmazsa, task değişkeni None olur
            return task["color"]  # Color değerini döndür
        else:
            print(f"Görev ID {task_id} bulunamadı!")
            return None
