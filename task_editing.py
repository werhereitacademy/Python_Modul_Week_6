from task_management import TaskManagement

class TaskEditing:
    def __init__(self, task_management):
        self.task_management = task_management

    def find_task(self, task_id):
        for task in self.task_management.task_list:
            if task["task_id"] == task_id:
                return task
        return f"Task with ID {task_id} not found!"

    def set_task_status(self, task_id, status):
        task = self.find_task(task_id)
        if task:
            task["task_status"] = status
            print(f"Task {task_id} status updated to: {status}")
        else:
            print(f"Task {task_id} not found!")

    def set_prioritization(self, task_id, priority):
        task = self.find_task(task_id)
        if task:
            task["priority"] = priority
            print(f"Task {task_id} priority updated to: {priority}")
        else:
            print(f"Task {task_id} not found!")

    def set_new_deadline(self, task_id, deadline):
        task = self.find_task(task_id)
        if task:
            task["deadline"] = deadline
            print(f"Task {task_id} deadline updated to: {deadline}")
        else:
            print(f"Task {task_id} not found!")


    def mark_status_completed(self, task_id):
        task = self.find_task(task_id)
        if task:
            task["task_status"] = "Completed"
            return True
        else:
                return False


    def get_task_by_id(self, task_id):
        task = self.find_task(task_id)
        if task:
            return f"Task ID: {task_id}, Name: {task['task_name']}, Deadline: {task['deadline']}, Priority: {task['priority']}, Color: {task['task_color']}"
        return f"Task {task_id} not found!" 
    
task_management = TaskManagement()
te = TaskEditing(task_management)
te.set_task_status(1, "In Progress")
te.mark_status_completed(2)
te.set_prioritization(2, "High")
te.set_new_deadline(1, "2025-02-01")
task_info = te.get_task_by_id(1)
print(task_info)