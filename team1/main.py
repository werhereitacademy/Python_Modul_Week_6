from task_editting import TaskEditing  
from task_management import TaskManagement  
def main():
    task_manager = TaskEditing()  # Mevcut görevleri yönetmek için
    task_creator = TaskManagement()  # Yeni görevler eklemek için

    while True:
        print("\n=== GÖREV YÖNETİM SİSTEMİ ===")
        print("1. Yeni Gorev Ekle")
        print("2. Gorev Durumunu Guncelle")
        print("3. Gorev Onceligini Guncelle")
        print("4. Gorev Son Teslim Tarihini Guncelle")
        print("5. Gorevi Sil")
        print("6. CIKIS")

        secim = input("Yapmak istediginiz islemi seçin (1-6): ")

        if secim == "1":  # ✅ Yeni görev ekleme işlemi
            task_name = input("Gorev adi: ")
            description = input("Gorev açiklamasi: ")
            priority = input("Oncelik (High/Low): ")
            deadline = input("Son teslim tarihi (YYYY-AA-GG): ")
            task_type = input("Gorev Tipi(Personal/Work): ")

            task_creator.add_task(task_name, task_type, description, priority, deadline)
            print("✅ Yeni gorev basariyla eklendi!")

        elif secim == "2":  # Görev durumu güncelleme
            task_id = int(input("Gorev ID'sini girin: "))
            print("Durum seçenekleri: 1- Beklemede, 2- Devam Ediyor, 3- Tamamlandı")
            status = int(input("Yeni durumu girin (1-3): "))
            task_manager.set_task_status(task_id, status)

        elif secim == "3":  # Öncelik güncelleme
            task_id = int(input("Görev ID'sini girin: "))
            priority = input("Yeni önceligi girin (High/Low): ")
            task_manager.set_task_priority(task_id, priority)

        elif secim == "4":  # Son teslim tarihini güncelleme
            task_id = int(input("Görev ID'sini girin: "))
            deadline = input("Yeni teslim tarihini girin (YYYY-AA-GG): ")
            task_manager.set_task_deadline(task_id, deadline)

        elif secim == "5":  # Görev silme
            task_id = int(input("Silmek istediginiz gorev ID'sini girin: "))
            task_manager.remove_task(task_id)

        elif secim == "6":  # Çıkış
            print("Cikis yapiliyor...")
            break

        else:
            print("❌ Geçersiz seçim, lütfen tekrar deneyin!")

main()