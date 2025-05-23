class TaskEditing: #Yunus
    def update_status(self, task, new_task_status):
        task.task_status = new_task_status
        task.auto_set_color()
        print(f"Görev durumu güncellendi. Yeni renk: {task.task_color}")

    def update_priority(self, task, new_task_priority):
        task.task_priority = new_task_priority

    def update_deadline(self, task, new_task_deadline):
        task.task_deadline = new_task_deadline