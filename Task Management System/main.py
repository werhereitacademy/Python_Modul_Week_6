import task_management as tm
import task_editing as te
import task_tracking as tt
import menu

# Geçerli bir sayısal giriş yapılmasını sağlar.
def get_user_choice(message="Lütfen bir işlem numarası giriniz: "):
    while True:
        try:
            return  int(input(message))
        except Exception as e:
            print(f"Geçersiz giriş: {e}")

def get_available_id(tm1):
    """
    Bu fonksiyon, mevcut görevlerin ID'lerini kontrol eder ve kullanılabilir en küçük ID'yi döndürür.
    """
    task_ids = [task.id for task in tm1.tasks]
    if not task_ids:
        return 1
    return min(set(range(1, max(task_ids) + 2)) - set(task_ids))


def add_task(tm1):
    menu.header("➕   Add a New Task")
    try:
        task_id = get_available_id(tm1)
        task_name = input("Görev adı: ")
        deadline = input("Görev son tarihi (YYYY-MM-DD): ")
        
        task_type = input("Görev türü (1: Kişisel, 2: İş): ")
        if task_type == "1":
            tsk = PersonalTask()
        elif task_type == "2":
            tsk = Worktask()
        else:
            raise ValueError("Geçersiz görev türü.")

        tm1.add_task(tsk)
        print("Görev başarıyla eklendi.")
    except Exception as e:
        print(f"Geçersiz giriş: {e}")

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
        menu.display_main_menu()

        choice = get_user_choice()

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