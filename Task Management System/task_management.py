class TaskManagement:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def display_tasks(self):
        for task in self.task_list:
            print(f"ID: {task.task_id}, Name: {task.task_name}, Deadline: {task.deadline}, Status: {task.status}, Priority: {task.priority}, Color: {task.color}")