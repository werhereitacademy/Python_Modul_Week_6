# Görev Düzenleme Sınıfı
class TaskEditing:
    def __init__(self, manager):
        self.manager = manager

    def mark_complete(self, title):
        for task in self.manager.task_list:
            if task.title == title:
                task.completed = True
                return f"'{title}' tamamlandı."
        return "Görev bulunamadı."

    def remove_task(self, title):
        self.manager.task_list = [task for task in self.manager.task_list if task.title != title]
        return f"'{title}' silindi."

    def update_priority(self, title, new_priority):
        for task in self.manager.task_list:
            if task.title == title:
                task.priority = new_priority
                return f"'{title}' önceliği '{new_priority}' olarak güncellendi."
        return "Görev bulunamadı."

    def update_deadline(self, title, new_deadline):
        for task in self.manager.task_list:
            if task.title == title:
                task.deadline = SPECIAL_KEYWORDS.get(new_deadline, new_deadline)
                return f"'{title}' son tarihi '{new_deadline}' olarak güncellendi."
        return "Görev bulunamadı."

    def search_task(self, title):
        for task in self.manager.task_list:
            if task.title == title:
                return task.display_info()
        return "Görev bulunamadı."

