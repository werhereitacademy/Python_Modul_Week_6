import json

class TaskManager:
    def __init__(self, filename="gorevler.json"):
        """TaskManager sınıfını başlatır, verilen dosyayı okur veya yeni bir dosya oluşturur."""
        self.filename = filename
        self.task_list = self.load_tasks()

    def load_tasks(self):
        """Verilen JSON dosyasındaki görevleri okur ve bir liste döndürür."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)  # JSON verisini okur ve Python listesine dönüştürür
        except (FileNotFoundError, json.JSONDecodeError):
            # Dosya yoksa veya JSON geçersizse boş bir liste döndürür
            return []

    def save_tasks(self):
        """Görevleri JSON dosyasına kaydeder."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.task_list, file, ensure_ascii=False, indent=4)

    def add_task(self, task):
        """Yeni bir görev ekler ve ardından görevleri dosyaya kaydeder."""
        self.task_list.append(task)  # Yeni görevi listeye ekler
        self.save_tasks()  # Güncellenmiş listeyi dosyaya kaydeder

    def display_tasks(self):
        """Tüm görevleri ekrana yazdırır."""
        if self.task_list:
            for task in self.task_list:
                print(f"ID: {task['id']}, Ad: {task['ad']}, Öncelik: {task['oncelik']}, Son Tarih: {task['son_tarih']}")
        else:
            print("Görev listesi boş.")

# Ana program:
if __name__ == "__main__":
    task_manager = TaskManager()

    # Yeni görevler ekleme
    task_manager.add_task({"id": 1, "ad": "Görev 1", "oncelik": "yüksek", "son_tarih": "2025-01-30"})
    task_manager.add_task({"id": 2, "ad": "Görev 2", "oncelik": "orta", "son_tarih": "2025-02-05"})

    # Tüm görevleri ekrana yazdırma
    print("Tüm Görevler:")
    task_manager.display_tasks()
