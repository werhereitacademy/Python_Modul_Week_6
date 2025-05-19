import task_management as tm
import task_editing as te
import task_tracking as tt
from task import *
from datetime import datetime
import menu


def get_available_id(tm1):
    """
    Bu fonksiyon, mevcut görevlerin ID'lerini kontrol eder ve kullanılabilir en küçük ID'yi döndürür.
    """
    task_ids = [task.id for task in tm1.tasks]
    if not task_ids:
        return 1
    return min(set(range(1, max(task_ids) + 2)) - set(task_ids))


def get_date_input(prompt):
    while True:
        date_input = input(f"{prompt} (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("⚠️ Geçersiz tarih formatı. Örn: 2025-12-01")

def get_nonempty_input(prompt):
    while True:
        data = input(prompt).strip()
        if data:
            return data
        else:
            print("⚠️ Bu alan boş bırakılamaz.")

def add_task(tm1):
    menu.header("➕   Yeni Görev Ekle")
    try:
        task_id = get_available_id(tm1)
        name = get_nonempty_input("Görev Adı: ")
        deadline = get_date_input("Görev Son Tarihi")

        status = menu.show_options("Durum Seçiniz", {
            "1": "Tamamlandı",
            "2": "Devam Ediyor",
            "3": "Beklemede"
        })

        priority = menu.show_options("Öncelik Seçiniz", {
            "1": "Düşük",
            "2": "Orta",
            "3": "Yüksek"
        })

        task_type = menu.show_options("Görev Türü", {
            "1": "Kişisel Görev",
            "2": "İş Görevi"
        })

        if task_type == "Kişisel Görev":
            task = PersonalTask(task_id, name, deadline, status, priority)
        else:
            task = WorkTask(task_id, name, deadline, status, priority)

        tm1.add_task(task)
        print("\n✅ Görev başarıyla eklendi.")

    except Exception as e:
        print(f"\n❌ Hata: {e}")


def edit_task(tm1):
    tm1.display_tasks()
    task_id = int(input("Düzenlemek istediğiniz görev ID'sini girin: "))
    task = tm1.get_task(task_id)
    menu.header("✏️   Edit a Task")
    try:
        task.task_name = input("Yeni görev açıklaması: ")
        task.set_new_date(input("Yeni görev son tarihi (YYYY-MM-DD): "))
        tm1.edit_task(task_id, task_name, task_description, task_deadline)
        print("Görev başarıyla güncellendi.")
    except Exception as e:
        print(f"Geçersiz giriş: {e}")

def track_task(tm1):
    menu.header("📊   Track a Task")
    try:
        task_id = int(input("Takip etmek istediğiniz görev ID'sini girin: "))
        task = tm1.track_task(task_id)
        if task:
            print(f"ID: {task['id']}, Adı: {task['name']}, Açıklama: {task['description']}, Son Tarih: {task['deadline']}")
        else:
            print("Görev bulunamadı.")
    except Exception as e:
        print(f"Geçersiz giriş: {e}")

def main():
    tm1 = tm.TaskManagement()
    while True:
        choice = menu.display_main_menu()

        if choice == 1:
            add_task(tm1)
        elif choice == 2:
            edit_task(tm1)
        elif choice == 3:
            track_task(tm1)
        if choice == 0:
            print("Programdan çıkılıyor...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  