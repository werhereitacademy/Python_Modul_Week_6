from personal_task import PersonalTask
from work_task import WorkTask
from task_management import TaskManagement
from task_editing import TaskEditing
from task_tracking import TaskTracking
from keywords import SPECIAL_KEYWORDS
from datetime import datetime

def get_date_input():
    user_input = input("Enter deadline (YYYY-MM-DD or keywords: today, tomorrow, next week): ").lower()
    if user_input in SPECIAL_KEYWORDS:
        return SPECIAL_KEYWORDS[user_input].strftime("%Y-%m-%d")
    try:
        datetime.strptime(user_input, "%Y-%m-%d")
        return user_input
    except ValueError:
        print("Invalid date format.")
        return get_date_input()

def main():
    tm = TaskManagement()
    te = TaskEditing(tm)
    tt = TaskTracking(tm)

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Personal Task")
        print("2. Add Work Task")
        print("3. Display Tasks")
        print("4. Set Task Status")
        print("5. Mark Task as Completed")
        print("6. Set Task Priority")
        print("7. Get Task Deadline")
        print("8. Get Task Color")
        print("9. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            task_id = input("Enter task ID: ")
            name = input("Enter task name: ")
            deadline = get_date_input()
            task = PersonalTask(task_id, name, deadline)
            tm.add_task(task)

        elif choice == "2":
            task_id = input("Enter task ID: ")
            name = input("Enter task name: ")
            deadline = get_date_input()
            task = WorkTask(task_id, name, deadline)
            tm.add_task(task)

        elif choice == "3":
            tm.display_tasks()

        elif choice == "4":
            task_id = input("Enter task ID: ")
            status = input("Enter new status: ")
            te.set_status(task_id, status)

        elif choice == "5":
            task_id = input("Enter task ID: ")
            te.mark_completed(task_id)

        elif choice == "6":
            task_id = input("Enter task ID: ")
            priority = input("Enter new priority: ")
            te.set_priority(task_id, priority)

        elif choice == "7":
            task_id = input("Enter task ID: ")
            deadline = tt.get_deadline(task_id)
            print(f"Deadline: {deadline}" if deadline else "Task not found.")

        elif choice == "8":
            task_id = input("Enter task ID: ")
            color = tt.get_color(task_id)
            print(f"Color: {color}" if color else "Task not found.")

        elif choice == "9":
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
