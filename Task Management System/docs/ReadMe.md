# 🧠 Task Management System

> Basit ama modüler yapıda, sınıf temelli bir Python görev yönetimi uygulaması.  
> Geliştirici takım olarak her birimiz belirli modüllerden sorumluyuz.

---

## 📌 Proje Amacı

Bu proje, görev oluşturma, düzenleme, takip etme ve sınıflara ayırma işlemlerini nesne yönelimli programlama prensiplerine uygun olarak gerçekleştirmeyi amaçlamaktadır.

---

## 🧩 UML Diyagramı

```plantuml
@startuml
abstract class Task {
    - task_id: int
    - task_name: str
    - deadline: str
    - status: str
    - priority: str
    - color: str
    + days_to_accomplish_task(): int
    + color_your_task(): str
}

class PersonalTask {
    + color_your_task(): str
}

class WorkTask {
    + color_your_task(): str
}

class TaskManagement {
    - task_list: List[Task]
    + add_task(task: Task): None
    + display_tasks(): None
}

class TaskEditing {
    - taskManagement
    + set_task_status(task_id: int, status: str): None
    + set_prioritization(task_id: int, priority: str): None
    + set_new_date(task_id: int, deadline: str): None
    + mark_status_completed(task_id: int): None
    + get_task_by_id(task_id: int): Task | None
}

class TaskTracking {
    - taskManagement
    + get_task_status(task_id: int): None
    + get_task_deadline(task_id: int): None
    + get_task_color(task_id: int): None
    + get_task_by_id(task_id: int): Task | None
}

class chief {
    .. Imports all modules ..
    .. Creates TaskManagement ..
    .. Creates & adds tasks ..
    .. Uses TaskEditing & Tracking ..
}

Task <|-- PersonalTask
Task <|-- WorkTask
TaskManagement *-- Task
TaskEditing --> TaskManagement
TaskTracking --> TaskManagement
chief --> TaskEditing
chief --> TaskTracking
chief --> TaskManagement
@enduml


| Üye Adı     | Sorumlu Sınıf(lar)                 | Açıklama                              |
| ----------- | ---------------------------------- | ------------------------------------- |
| **Ali**     | `Task`, `PersonalTask`, `WorkTask` | Soyut görev yapısı ve kalıtım sistemi |
| **Furkan**  | `TaskManagement`                   | Görevlerin listelenmesi ve eklenmesi  |
| **Mustafa** | `TaskTracking`                     | Görev takibi (renk, deadline, durum)  |
| **Lütfü**   | `TaskEditing`                      | Görev düzenleme işlemleri             |
| **Sen**     | `chief (main.py)`                  | Tüm modülleri kullanan kontrol birimi |


🛠️ Sınıf Açıklamaları
Task (abstract)
Ortak nitelikler: task_id, task_name, deadline, status, priority, color

Metotlar: days_to_accomplish_task(), color_your_task()

PersonalTask, WorkTask
Task sınıfından türetilmiştir.

color_your_task() override edilerek sabit bir renk döner.

TaskManagement
add_task(task: Task)

display_tasks()

TaskTracking
get_task_status(task_id)

get_task_color(task_id)

get_task_deadline(task_id)

TaskEditing
set_task_status, set_prioritization, set_new_date, mark_status_completed

🧪 Örnek Kullanım (main.py içinde)
python
Kopyala
Düzenle
from task import PersonalTask, WorkTask
from task_management import TaskManagement
from task_editing import TaskEditing
from task_tracking import TaskTracking

if __name__ == "__main__":
    tm = TaskManagement()
    edit = TaskEditing(tm)
    track = TaskTracking(tm)

    task1 = PersonalTask(1, "Read book", "2025-05-20", "Not Started", "Low")
    task2 = WorkTask(2, "Submit report", "2025-05-25", "In Progress", "High")

    tm.add_task(task1)
    tm.add_task(task2)

    tm.display_tasks()
    track.get_task_color(1)
    edit.set_task_status(1, "Completed")
    track.get_task_status(1)
📁 Proje Yapısı
css
Kopyala
Düzenle
📦 project-root/
 ┣ 📄 main.py
 ┣ 📄 task.py
 ┣ 📄 task_management.py
 ┣ 📄 task_editing.py
 ┣ 📄 task_tracking.py
 ┣ 📄 README.md
✅ Gereksinimler
Python 3.10+

Gerekli paket yok, sadece standart kütüphaneler

📚 Kodlama Kuralları
Tüm sınıflar tip anotasyonu kullanmalı

task_id eşsiz olmalı

Her method için docstring yazılmalı

Gereksiz tekrarlar metotlaştırılmalı

✨ Geliştirme Önerileri
status ve priority alanlarını sabit değerlerle sınırlamak için Enum sınıfı kullanılabilir

Görevler .json ya da .csv formatında dışa aktarılabilir

GUI arayüz ile entegre edilebilir (PyQt6 / Tkinter)

📃 Lisans
MIT © 2025
Bu proje eğitim amaçlı geliştirilmiştir.