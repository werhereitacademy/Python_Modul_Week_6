from datetime import datetime, timedelta
from task_management import TaskManagement
from task_editing import TaskEditing
from task_tracking import TaskTracking
from task import PersonalTask, WorkTask

def parse_deadline(deadline_str):
    SPECIAL_KEYWORDS = {
    "today": datetime.now(),
    "tomorrow": datetime.now() + timedelta(days=1),
    "next week": datetime.now() + timedelta(days=7)
}
    deadline_str = deadline_str.lower()
    if deadline_str in SPECIAL_KEYWORDS:
        return SPECIAL_KEYWORDS[deadline_str]
    else:
        return datetime.strptime(deadline_str, "%Y-%m-%d")

def main():
    
    manager=TaskManagement()
    editor=TaskEditing()
    tracker=TaskTracking()
    
    
    while True:
        print("\n=== GÖREV YÖNETİM SİSTEMİ ===")
        print("1. Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Görev Düzenle")
        print("4. Görev Takip")
        print("5. Çıkış")
        print()
        
        secim=input('Seciminizi giriniz: ')
        
        if secim=='1':
            task_id = max([task.task_id for task in manager.task_list], default=0) + 1
            task_name=input('Gorev ismini giriniz: ')
            task_deadline_input=input('Gorevin miadini giriniz: ')
            try:
                task_deadline=parse_deadline(task_deadline_input)
            except ValueError:
                print("Tarih formati hatali! YYYY-MM-DD seklinde giriniz.")
                continue            
            task_type=input('Gorevin tipini giriniz: (personal/work) ')
            
            if task_type=='personal':
                task=PersonalTask(task_id,task_name,task_deadline)      #priority="Low" olarak PersonalTask class'inda default olarak belirlenecek. color ise Task isimli abstract 
            elif task_type=='work':                                     #class'da baslangicta  default olarak 'orange' olarak belirlenecek.
                task=WorkTask(task_id,task_name,task_deadline)
            else:
                print('Gecersiz bir gorev tipi! ')
                continue
            manager.add_task(task)
            print('Gorev eklendi...')
        
        elif secim=='2':
            manager.list_tasks()
        
        elif secim=='3':
            task_id=int(input('Duzenlenecek gorevin ID numarasini giriniz: '))
            task=manager.find_task_by_id(task_id)
            if task:
                VALID_STATUSES = ["pending", "late", "atf", "done"]
                VALID_PRIORITIES = ["low", "medium", "high"]
                new_task_status=input("Yeni gorev status'unu giriniz: ('pending'/'late'/'atf'(about to finish)/'done')")
                if new_task_status not in VALID_STATUSES:
                    print("Geçersiz durum!")
                    continue
                new_task_priority=input("Yeni oncelik: ")
                if new_task_priority not in VALID_PRIORITIES:
                    print("Geçersiz durum!")
                    continue
                new_task_deadline_input=input("Yeni miad (YYYY-MM-DD): ")
                try:
                    new_task_deadline=parse_deadline(new_task_deadline_input)
                except ValueError:
                    print("Tarih formatı hatalı! YYYY-MM-DD şeklinde giriniz.")
                    continue                    
                
                editor.update_status(task, new_task_status)
                editor.update_priority(task, new_task_priority)
                editor.update_deadline(task, new_task_deadline)
                print('Gorev Guncellendi...')
        
        elif secim=='4':
            task_id=int(input('Takip edilecek gorevin ID numarasini giriniz: '))
            task=manager.find_task_by_id(task_id)
            if task:
                print("Durum:", tracker.get_status(task))
                print("Son Tarih:", tracker.get_deadline(task).date())
                print("Renk:", tracker.get_color(task))
        
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        
        else:
            print('Gecersiz Secim!')
                
                
if __name__ == "__main__":
    main()



