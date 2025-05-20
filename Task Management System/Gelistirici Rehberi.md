🧾 Task Management Uygulaması – Geliştirici Rehberi

    Ali:    task.py
    Furkan: task_management.py
    Mustfa: task_tracking.py
    Lütfü:  task_editing.py

👤 Ali: Task, PersonalTask, WorkTask (Temel veri yapısı + kalıtım yapısı)
    🔶 Sorumluluğun:
        Task: Soyut sınıf. Ortak özellikleri ve metotları barındırır.

        PersonalTask, WorkTask: Bu sınıfı genişleten alt sınıflardır.

    ✅ Yapılacaklar:
        Task sınıfını ABC (Abstract Base Class)` ile tanımla:

        Python’da soyut sınıflar için from abc import ABC, abstractmethod kullanılır.

        En az bir @abstractmethod tanımlanmalı.

        Ortak nitelikleri tanımla (task_id, status, priority, vs.)

        Tüm görev türleri bu verilere sahip olacak.

        color_your_task() metodunu alt sınıflar override edecek şekilde bırak.

        PersonalTask: Mesela "Blue"

        WorkTask: "Red" gibi sabit renk döndürebilir.

🎯 Örnek Yapı:

from abc import ABC, abstractmethod
from datetime import datetime

class Task(ABC):
    def __init__(self, task_id: int, task_name: str, deadline: str, status: str, priority: str):
        self.task_id = task_id
        self.task_name = task_name
        self.deadline = deadline
        self.status = status
        self.priority = priority
        self.color = self.color_your_task()

    @abstractmethod
    def color_your_task(self) -> str:
        pass

    def days_to_accomplish_task(self) -> int:
        today = datetime.today()
        deadline_date = datetime.strptime(self.deadline, "%Y-%m-%d")
        return (deadline_date - today).days


class PersonalTask(Task):
    def color_your_task(self) -> str:
        return "Blue"

class WorkTask(Task):
    def color_your_task(self) -> str:
        return "Red"


👤 Furkan: TaskManagement (Görev listesinin kalbi)
    🔶 Sorumluluğun:
        Görevleri listeye eklemek, göstermek.

        Task türündeki objeleri yönetmek.

    ✅ Yapılacaklar:
        Listeyi List[Task] olarak oluştur.

        from typing import List kullanılmalı.

        Sadece Task veya alt sınıfları kabul edilmeli.

        Görev ekleme metodu: add_task(task: Task)

        Aynı task_id'ye sahip görev zaten varsa eklenmemeli.

        Görevleri yazdırma: display_tasks()

        Güzel formatlanmış bir çıktı olmalı (geliştirici kolay test edebilsin diye).

🎯 Örnek Yapı:

from typing import List

class TaskManagement:
    def __init__(self):
        self.task_list: List[Task] = []

    def add_task(self, task: Task) -> None:
        if any(t.task_id == task.task_id for t in self.task_list):
            print(f"Task ID {task.task_id} already exists.")
            return
        self.task_list.append(task)

    def display_tasks(self) -> None:
        for task in self.task_list:
            print(f"ID: {task.task_id}, Name: {task.task_name}, Status: {task.status}, Priority: {task.priority}")

            
👤 Mustafa: TaskTracking (Veri okuma – raporlama)
    🔶 Sorumluluğun:
    Görevlerin durumunu, rengini ve bitiş tarihini kullanıcıya sunmak.

    Görevleri TaskManagement üzerinden almalı.

    ✅ Yapılacaklar:
    TaskManagement nesnesini constructor'da al.

    get_task_by_id() ile görev bulma metodu yaz.
        Görev bulunamazsa None döndür.

    Durum/renk gibi bilgileri döndüren metodları oluştur.
        Bunlar sadece okuyucu olmalı, değiştirme yapmaz.

🎯 Örnek Yapı:

class TaskTracking:
    def __init__(self, task_management: TaskManagement):
        self.taskManagement = task_management

    def get_task_by_id(self, task_id: int) -> Task | None:
        for task in self.taskManagement.task_list:
            if task.task_id == task_id:
                return task
        return None

    def get_task_status(self, task_id: int) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            print(f"Task status: {task.status}")

    def get_task_color(self, task_id: int) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            print(f"Task color: {task.color}")


👤 Lütfü: TaskEditing (Veri güncelleme)
🔶 Sorumluluğun:  Görevlerin durumu, önceliği, son tarihi gibi bilgilerini değiştirmek.

    ✅ Yapılacaklar:
    TaskManagement nesnesine eriş.
    Her method görev olup olmadığını kontrol etmeli.
    Değişiklikleri doğrudan görev objesi üzerinden yap.

🎯 Örnek Yapı:
class TaskEditing:
    def __init__(self, task_management: TaskManagement):
        self.taskManagement = task_management

    def get_task_by_id(self, task_id: int) -> Task | None:
        for task in self.taskManagement.task_list:
            if task.task_id == task_id:
                return task
        return None

    def set_task_status(self, task_id: int, status: str) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            task.status = status

    def set_prioritization(self, task_id: int, priority: str) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            task.priority = priority

    def set_new_date(self, task_id: int, deadline: str) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            task.deadline = deadline

    def mark_status_completed(self, task_id: int) -> None:
        self.set_task_status(task_id, "Completed")


🧑‍💼 Sen:  (main.py )
    Yapacakların:
    Tüm sınıfları birleştir.
    Örnek görevler oluştur.

Görevleri ekle, durumu göster, değiştir, vs.

📌 Genel Kodlama Kuralları:
    ✅ Tüm task_id eşsiz olmalı.

    ✅ Giriş doğrulamaları (type check veya id kontrolü) unutulmamalı.

    🔁 Tekrar eden kodlar metotlaştırılmalı.

    🧪 __name__ == "__main__" bloğu kullanılmalı (main.py için).

    📚 Kodda yorum satırları, docstring ve tip anotasyonları kullanılmalı.