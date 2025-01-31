from task_editting import TaskEditing  
from task_management import TaskManagement  
from task_tracking import TaskTracking
def main():
    task_edittings = TaskEditing()  # Mevcut görevleri yönetmek için
    task_creator = TaskManagement()
    task_tracker = TaskTracking()  # Yeni görevler eklemek için

    while True:
        print("\n=== GÖREV YÖNETİM SİSTEMİ ===")
        print("1. Yeni Gorev Ekle")
        print("2. Gorev Durumunu Guncelle")
        print("3. Gorev Onceligini Guncelle")
        print("4. Gorev Son Teslim Tarihini Guncelle")
        print("5. Gorevi Sil")
        print("6. Gorev Bilgilerini Sorgula") 
        print("7. CIKIS")

        secim = input("Yapmak istediginiz islemi seçin (1-6): ")

        if secim == "1":  #  Yeni görev ekleme işlemi
            task_name = input("Gorev adi: ")
            deadline = input("Son teslim tarihi (YYYY-AA-GG): ")
            task_type = input("Gorev Tipi(Personal/Work): ")

            task_creator.add_task(task_type, task_name, deadline)
            print(" Yeni gorev basariyla eklendi!")

        elif secim == "2":  # Görev durumu güncelleme
            task_id = int(input("Gorev ID'sini girin: "))
            print("Durum seçenekleri: 1- Pending, 2- In Progress, 3- Completed")
            status = int(input("Yeni durumu girin (1-3): "))
            task_edittings.set_task_status(task_id, status)

        elif secim == "3":  # Öncelik güncelleme
            task_id = int(input("Görev ID'sini girin: "))
            priority = input("Yeni önceligi girin (High/Low): ")
            task_edittings.set_task_priority(task_id, priority)

        elif secim == "4":  # Son teslim tarihini güncelleme
            task_id = int(input("Görev ID'sini girin: "))
            new_deadline_date = input("Yeni teslim tarihini girin (YYYY-AA-GG): ")
            task_edittings.set_task_deadline(task_id, new_deadline_date)

        elif secim == "5":  # Görev silme
            task_id = int(input("Silmek istediginiz gorev ID'sini girin: "))
            task_edittings.remove_task(task_id)

        elif secim == "6":  # Görev bilgilerini sorgulama
            task_id = int(input("Sorgulamak istediğiniz görev ID'sini girin: "))
            print("1. Durumu sorgula")
            print("2. Teslim tarihini sorgula")
            print("3. Rengi sorgula")
            sorgulama_secim = input("Sorgulamak istediğiniz bilgiyi seçin (1-3): ")

            if sorgulama_secim == "1":
                status = task_tracker.get_task_status(task_id)
                if status:
                    print(f"Bu görevin durumu: {status}")
            elif sorgulama_secim == "2":
                deadline = task_tracker.get_task_deadline(task_id)
                if deadline:
                    print(f"Bu görevin teslim tarihi: {deadline}")
            elif sorgulama_secim == "3":
                color = task_tracker.get_task_color(task_id)
                if color:
                    print(f"Bu görevin rengi: {color}")
            else:
                print(" Geçersiz seçenek!")
        
        elif secim == "7":  # Çıkış
            print("Cikis yapiliyor...")
            break

        else:
            print("❌ Geçersiz seçim, lütfen tekrar deneyin!")

main()