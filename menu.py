from task_management import TaskManagement
from task_scheduling import TaskScheduling
from task_editing import TaskEditing
from task_tracking import TaskTracking



class Menu:
    def __init__(self):
        self.task_management = TaskManagement()
        self.task_scheduling = TaskScheduling(self.task_management)
        self.task_editing = TaskEditing(self.task_management)
        self.task_tracking = TaskTracking(self.task_management)

    def display_menu(self):
        while True:
            print("\nAna Menü")
            print("1. Görev Ekle")
            print("2. Görevleri Göster")
            print("3. Görev Güncelle")
            print("4. Görevi Tamamla")
            print("5. Çıkış")
            
            choice = input("Seçiminizi yapın (1-5): ")
            
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.task_management.display_tasks()
            elif choice == '3':
                self.edit_task()
            elif choice == '4':
                self.complete_task()
            elif choice == '5':
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")

    def add_task(self):
        id = input("Görev ID'si: ")
        type=input("Görev Turu(personal of work): ")
        name = input("Görev Adı: ")
        priority = input("Görev Önceliği: ")
        due_date = input("Görev Bitiş Tarihi: ")
        self.task_scheduling.create_task(id, type, name, priority, due_date)

    def edit_task(self):
        id = input("Güncellenecek Görev ID'si: ")
        new_type = input("Yeni Type Adı (work yada personal/ boş bırakmak için Enter'a basın): ")
        new_name = input("Yeni Görev Adı (boş bırakmak için Enter'a basın): ")
        new_priority = input("Yeni Görev Önceliği (boş bırakmak için Enter'a basın): ")
        new_due_date = input("Yeni Görev Bitiş Tarihi (boş bırakmak için Enter'a basın): ")
        self.task_editing.edit_task( id, new_type if new_type else None,
                                     new_name if new_name else None,
                                     new_priority if new_priority else None,
                                     new_due_date if new_due_date else None)

    def complete_task(self):
        id = input("Tamamlanacak Görev ID'si: ")
        self.task_tracking.mark_task_complete(id)

# Programı çalıştır
if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()