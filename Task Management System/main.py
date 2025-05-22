import task_management as tm
import task_editing as te
import task_tracking as tt
from task import *
from datetime import datetime
import menu
from file_io import *
from typing import List


def load_tasks_from_file(file_path: str) -> List[Task]:
    """
    Load tasks from a JSON file and return a list of Task objects.
    
    Args:
        file_path (str): Path to the JSON file containing tasks.
    
    Returns:
        List[Task]: A list of task objects (PersonalTask or WorkTask).
    """
    tasks = read_json(file_path)
    tasks = sorted(tasks, key=lambda x: x["task_id"])
    task_list = []
    for task in tasks:
        if task['task_type'] == 'PersonalTask':
            task_obj = PersonalTask(
                task_id=task['task_id'],
                task_name=task['task_name'],
                deadline=task['deadline'],
                status=task['status'],
                priority=task['priority'],
            )
        elif task['task_type'] == 'WorkTask':
            task_obj = WorkTask(
                task_id=task['task_id'],
                task_name=task['task_name'],
                deadline=task['deadline'],
                status=task['status'],
                priority=task['priority'],
            )
        else:
            continue
        task_list.append(task_obj)
    return task_list


def save_tasks_to_file(file_path: str, task_list: List[Task]) -> None:
    """
    Save a list of Task objects to a JSON file.
    
    Args:
        file_path (str): Path to the JSON file to save tasks.
        task_list (List[Task]): List of task objects to be saved.
    """
    tasks = []
    for task in task_list:
        task_data = {
            'task_type': type(task).__name__,
            'task_id': task.task_id,
            'task_name': task.task_name,
            'deadline': task.deadline,
            'status': task.status,
            'priority': task.priority,
            'color': task.color
        }
        tasks.append(task_data)
    write_json(file_path, tasks)


def get_available_id(tm1: tm.TaskManagement) -> int:
    """
    Get the smallest available task ID that is not currently used.
    
    Args:
        tm1 (TaskManagement): The task management object.
    
    Returns:
        int: The next available task ID.
    """
    task_ids = [task.task_id for task in tm1.task_list]
    if not task_ids:
        return 1
    return min(set(range(1, max(task_ids) + 2)) - set(task_ids))


def get_date_input(prompt: str) -> str:
    """
    Prompt the user to enter a valid date string in YYYY-MM-DD format.
    
    Args:
        prompt (str): The message to display to the user.
    
    Returns:
        str: A valid date string.
    """
    while True:
        date_input = input(f"{prompt} (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            menu.show_message("⚠️ Invalid date format. Example: 2025-12-01")


def get_nonempty_input(prompt: str) -> str:
    """
    Prompt the user until they provide a non-empty input.
    
    Args:
        prompt (str): The message to display to the user.
    
    Returns:
        str: The user input.
    """
    while True:
        data = input(prompt).strip()
        if data:
            return data
        else:
            menu.show_message("⚠️ This field cannot be empty.")


def show_tasks(tm1: tm.TaskManagement) -> None:
    """
    Display the list of tasks in a tabular format.
    
    Args:
        tm1 (TaskManagement): The task management object.
    """
    ttrack = tt.TaskTracking(tm1)
    tlist = tm1.task_list
    if not tlist:
        menu.show_message("⚠️ No tasks available.")
        return
    column_names = ["🆔 ID", "📌 Name", "📅 Deadline", "📊 Status", "⚡ Priority"]
    menu.show_list("📋   Task List", column_names, tlist)
    menu.show_message("")


def add_task(file_path: str, tm1: tm.TaskManagement) -> None:
    """
    Add a new task and save it to file.
    
    Args:
        file_path (str): Path to the JSON file to save the task.
        tm1 (TaskManagement): The task management object.
    """
    menu.header("➕   Add a New Task")
    try:
        task_id = get_available_id(tm1)
        name = get_nonempty_input("Task Name: ")
        deadline = get_date_input("Task Deadline")

        status = menu.show_options("Select Status", {
            "1": "Completed",
            "2": "In Progress",
            "3": "Pending"
        })

        priority = menu.show_options("Select Priority", {
            "1": "Low",
            "2": "Medium",
            "3": "High"
        })

        task_type = menu.show_options("Select Task Type", {
            "1": "Personal Task",
            "2": "Work Task"
        })

        if task_type == "Personal Task":
            task = PersonalTask(task_id, name, deadline, status, priority)
        else:
            task = WorkTask(task_id, name, deadline, status, priority)

        tm1.add_task(task)
        save_tasks_to_file(file_path, tm1.task_list)
        menu.show_message(f"\n✅ Task added successfully with ID: {task_id}")

    except Exception as e:
        menu.show_message(f"\n❌ Error: {e}")


def edit_task(tm1: tm.TaskManagement) -> None:
    """
    Edit an existing task's status, priority, deadline, or mark it as completed.
    
    Args:
        tm1 (TaskManagement): The task management object.
    """
    tedit = te.TaskEditing(tm1)
    menu.header("✏️   Edit a Task")
    tm1.display_tasks()
    task_id = int(input("\nEnter the ID of the task you want to edit: "))
    task_to_edit = tedit.get_task_by_id(task_id)
    if not task_to_edit:
        menu.show_message("⚠️ Task not found.")
        return

    editing_option = menu.show_options("Select an option to edit", {
        "1": "Set Task Status",
        "2": "Set Priority",
        "3": "Set New Deadline",
        "4": "Mark Task as Completed"
    })

    if editing_option == "1":
        new_status = menu.show_options("Select New Status", {
            "1": "Completed",
            "2": "In Progress",
            "3": "Pending"
        })
        tedit.set_task_status(task_id, new_status)
    elif editing_option == "2":
        new_priority = menu.show_options("Select New Priority", {
            "1": "Low",
            "2": "Medium",
            "3": "High"
        })
        tedit.set_prioritization(task_id, new_priority)
    elif editing_option == "3":
        new_deadline = get_date_input("Enter New Deadline")
        tedit.set_new_date(task_id, new_deadline)
    elif editing_option == "4":
        tedit.mark_status_completed(task_id)
    else:
        menu.show_message("⚠️ Invalid option selected.")
        return

    print("✅ Task updated successfully.")
    menu.show_message(
        f"🆔 ID: {task_to_edit.task_id}\n"
        f"📌 Name: {task_to_edit.task_name}\n"
        f"📊 Status: {task_to_edit.status}\n"
        f"⚡ Priority: {task_to_edit.priority}\n"
        f"📅 Deadline: {task_to_edit.deadline}"
    )


def main() -> None:
    """
    Entry point of the task manager application.
    Handles loading tasks, displaying menu, and responding to user choices.
    """
    tm1 = tm.TaskManagement()
    task_file = 'tasks.json'
    tm1.task_list = load_tasks_from_file(task_file)

    while True:
        choice = menu.display_main_menu()

        if choice == "1":
            menu.header("📋   Task List")
            show_tasks(tm1)
        elif choice == "2":
            add_task(task_file, tm1)
        elif choice == "3":
            edit_task(tm1)
        elif choice == "0":
            print("Exiting the program...\n")
            break


if __name__ == "__main__":
    main()