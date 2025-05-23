class TaskEditing:
    # Constructor: receives a list of all tasks and stores it
    # Constructor: ontvangt een lijst met alle taken en slaat deze op
    def __init__(self, task_list):
        self.task_list = task_list

    # Find a task by its ID
    # Zoek een taak op basis van het ID
    def find_task(self, task_id):
        for task in self.task_list:
            if task.task_id == task_id:
                return task
        raise ValueError("Task not found.")  # Taak niet gevonden

    # Update the status of a task (e.g., from Pending to Completed)
    # Wijzig de status van een taak (bijv. van 'In afwachting' naar 'Voltooid')
    def update_status(self, task_id, new_status):
        task = self.find_task(task_id)
        task.status = new_status
        print(f"The status of '{task.task_name}' has been updated to '{new_status}'.")
        # De status van '{task.task_name}' is bijgewerkt naar '{new_status}'

    # Update the priority of a task (e.g., Low, Medium, High)
    # Wijzig de prioriteit van een taak (bijv. Laag, Gemiddeld, Hoog)
    def update_priority(self, task_id, new_priority):
        task = self.find_task(task_id)
        task.priority = new_priority
        print(f"The priority of '{task.task_name}' has been updated to '{new_priority}'.")
        # De prioriteit van '{task.task_name}' is bijgewerkt naar '{new_priority}'

    # Update the deadline of a task (e.g., change due date)
    # Wijzig de deadline van een taak (bijv. wijzig de einddatum)
    def update_deadline(self, task_id, new_deadline):
        task = self.find_task(task_id)
        task.deadline = new_deadline
        print(f"The deadline of '{task.task_name}' has been updated to '{new_deadline}'.")
        # De deadline van '{task.task_name}' is bijgewerkt naar '{new_deadline}'
