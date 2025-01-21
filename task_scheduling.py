from task_types import PersonalTask, WorkTask
from task_management import TaskManagement
from datetime import datetime, timedelta

SPECIAL_KEYWORDS = {
    "today": datetime.now().strftime("%Y-%m-%d"),
    "tomorrow": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
    "next week": (datetime.now() + timedelta(weeks=1)).strftime("%Y-%m-%d")
}

# class TaskScheduling: