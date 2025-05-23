from typing import List
from task import Task  

class TaskManagement:
    """
    Manages a list of tasks and provides methods to add, retrieve, and display them.
    
    Attributes:
        task_list (List[Task]): A list of all task objects.
    """

    def __init__(self) -> None:
        """
        Initialize an empty task list.
        """
        self.task_list: List[Task] = []

    def add_task(self, task: Task) -> None:
        """
        Add a task to the task list.

        Args:
            task (Task): The task object to be added.
        """
        self.task_list.append(task)

    def get_task_by_id(self, task_id: int) -> Task:
        """
        Retrieve a task by its unique ID.

        Args:
            task_id (int): The ID of the task to retrieve.

        Returns:
            Task: The task object with the specified ID.

        Raises:
            ValueError: If no task with the given ID is found.
        """
        for task in self.task_list:
            if task.task_id == task_id:
                return task
        raise ValueError(f"No task found with ID: {task_id}")
