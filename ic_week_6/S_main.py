from S_task_management import TaskManagement
from S_task_editing import TaskEditing
from S_task_tracking import TaskTracking
from S_personal_task import PersonalTask
from S_work_task import WorkTask

# Task management sistemi oluştur
t1 = TaskManagement()

# Düzenleme ve takip sınıfları
te = TaskEditing(t1)
tt = TaskTracking(t1)

# Görevleri oluştur
p1 = PersonalTask(1, "P1", "2025-03-20")
w1 = WorkTask(2, "W2", "2025-02-25")

# Görevleri ekle
t1.add_task(p1)
t1.add_task(w1)

# Görevleri göster
t1.display_tasks()

# Görevleri düzenle
te.set_task_status(1, "In Progress")
te.mark_status_completed(1)
te.set_prioritization(1, "Not Important")

# Bilgi sorgulama
tt.get_task_deadline(1)
tt.get_task_color(2)

# Son haliyle görevleri tekrar göster
t1.display_tasks()
