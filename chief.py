# CHIEF

from task import PersonalTask, WorkTask  # Görev sınıfları
from task_management import TaskManagement
from task_editing import TaskEditing
from task_tracking import TaskTracking
from datetime import datetime


class Chief:
    def __init__(self):
        self.task_manager = TaskManagement()
        self.task_editor = TaskEditing(self.task_manager)
        self.task_tracker = TaskTracking(self.task_manager)

    def run_tests(self):
        """Programı test etmek için ana metot."""
        # Görev oluşturma
        task1 = PersonalTask(1, "Read a book", datetime(2025, 1, 25))
        task2 = WorkTask(2, "Complete project", datetime(2025, 1, 20))

        # Görevleri ekleme
        self.task_manager.add_task(task1)
        self.task_manager.add_task(task2)

        # Görev düzenleme
        self.task_editor.set_task_status(1, "In Progress")
        self.task_editor.set_prioritization(2, "Critical")
        self.task_editor.set_new_date(2, datetime(2025, 2, 1))
        self.task_editor.mark_status_completed(1)

        # Görev izleme
        self.task_tracker.get_task_status(1)
        self.task_tracker.get_task_deadline(2)
        self.task_tracker.get_task_color(1)

        # Tüm görevleri listeleme
        self.task_manager.display_tasks()


# Chief'i başlat ve testleri çalıştır
if __name__ == "__main__":
    chief = Chief()
    chief.run_tests()


