
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

class TaskEditing():
    def __init__(self):
        self.task_list = file_upload()
        self.status_map={1:"beklemede",2:"devam ediyor",3:"tamamlandi"}

    def set_task_status(self,task_id,status):#durum degistirme
        if status not in self.status_map:
            print("Geçersiz durum! Lütfen 1, 2 veya 3 giriniz.")
            return

        for task in self.task_list:
            if task["task_id"]==task_id:
                task["status"]=self.status_map[status]#yeni durumu atiyoruz 
                print(f"gorev durumu basari ile degistirildi yeni durum:{self.status_map[status]}")
                file_save(self.task_list)
                return
        
        print("gorev bulunamadi")
  
    
    def set_task_priority(self,task_id,priority):#oncelik degistirme
        oncelik_degerleri={"High" : "High","Low": "Low"}
        
        if priority not in oncelik_degerleri:
            print("Gecersiz oncelik degeri! Lutfen High veya Low giriniz.")
            return

        for task in self.task_list:
            if task["task_id"] == task_id:
                task["priority"] = oncelik_degerleri[priority]
                print(f"Gorev onceligi basari ile degistirildi. Yeni oncelik: {oncelik_degerleri[priority]}")
                file_save(self.task_list)
                return 

        print("Gorev bulunamadi!")


    def set_task_deadline(self,task_id,deadline):#deadline degistirme
        today = date.today()
        try:
            new_deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()
           

            if new_deadline_date < today:
                print("Gecersiz deadline! Lutfen bugunden sonraki bir tarih giriniz.")
                return

            for task in self.task_list:
                if task["task_id"] == task_id:
                    task["deadline"] = new_deadline_date
                    print(f"Gorev deadline basari ile degistirildi. Yeni deadline: {new_deadline_date}")
                    file_save(self.task_list)  
                    return

            print("Gorev bulunamadi!")



        except ValueError:
            print("Gecersiz deadline! Lutfen YYYY-AA-GG formatinda bir tarih giriniz.")

    def remove_task(self,task_id):#task silme
        for task in self.task_list:
            if task["task_id"] == task_id:
                self.task_list.remove(task)
                file_save(self.task_list)
                print("Gorev basari ile silindi.")
                return
        print("Gorev bulunamadi!")   