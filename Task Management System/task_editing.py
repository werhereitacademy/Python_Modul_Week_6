from task_management import TaskManagement
from task import Task 

class TaskEditing:
    """
    A class to handle editing operations for tasks such as status, priority, and deadlines.
    
    Attributes:
        taskManagement (TaskManagement): An instance of TaskManagement which contains the task list.
    """

    def __init__(self, tm: TaskManagement) -> None:
        """
        Initialize the TaskEditing instance with a TaskManagement object.

        Args:
            tm (TaskManagement): The task management instance containing all tasks.
        """
        self.taskManagement = tm

    def find_task(self, task_id: int) -> Task:
        """
        Find and return a task by its ID.

        Args:
            task_id (int): The unique ID of the task.

        Returns:
            Task: The task object that matches the given ID.

        Raises:
            ValueError: If the task with the specified ID is not found.
        """
        return self.taskManagement.get_task_by_id(task_id)
    

    def update_status(self, task_id: int, new_status: str) -> None:
        """
        Update the status of a specific task.

        Args:
            task_id (int): The ID of the task to update.
            new_status (str): The new status to assign to the task.
        """
        task = self.find_task(task_id)
        task.status = new_status
        

    def mark_status_completed(self, task_id: int) -> None:
        """
        Mark a task's status as 'Completed'.

        Args:
            task_id (int): The ID of the task to update.
        """
        self.update_status(task_id, "Completed")

    def update_priority(self, task_id: int, new_priority: str) -> None:
        """
        Update the priority level of a specific task.

        Args:
            task_id (int): The ID of the task to update.
            new_priority (str): The new priority value (e.g., Low, Medium, High).
        """
        task = self.find_task(task_id)
        task.priority = new_priority
        

    def update_deadline(self, task_id: int, new_deadline: str) -> None:
        """
        Update the deadline of a specific task.

        Args:
            task_id (int): The ID of the task to update.
            new_deadline (str): The new deadline in 'YYYY-MM-DD' format.
        """
        task = self.find_task(task_id)
        task.deadline = new_deadline
        
