from task_management import TaskManagement
from task_scheduling import TaskScheduling
from task_editing import TaskEditing
from task_tracking import TaskTracking

def main():
    # TaskManagement nesnesi 
    task_manager = TaskManagement()

    # Görev Planlayıcı ve Düzenleyici nesneleri 
    task_scheduling = TaskScheduling(task_manager)
    task_editing = TaskEditing(task_manager)
    task_tracking = TaskTracking(task_manager)

    # Uygulamayı başlat
    task_manager.start_app()

    # Yeni bir görev ekle (kişisel görev)
    task_scheduling.create_task(
        type="personal",
        id=1,
        name="Alışveriş",
        priority="Yüksek",
        due_date="2024-10-15")

    # Yeni bir görev ekle (iş görevi)
    task_scheduling.create_task(
        type="work",
        id=2,
        name="Proje Raporu",
        priority="Orta",
        due_date="2024-10-20")

    # Görev listesi görüntüleniyor
    print("\n--- Mevcut Görevler ---")
    task_manager.display_tasks()

    # Görevi düzenle
    task_editing.edit_task(
        id=1,
        new_name="Market Alışverişi",
        new_due_date="2024-10-16")

    # Görev listesi yeniden görüntüleniyor
    print("\n--- Güncellenmiş Görevler ---")
    task_manager.display_tasks()

    # Görevi tamamlanmış olarak işaretle
    task_tracking.mark_task_complete(id=1)

    # Son durumu görüntüle
    print("\n--- Tamamlanmış Görevler ---")
    task_manager.display_tasks()

if __name__ == "__main__":
    main()