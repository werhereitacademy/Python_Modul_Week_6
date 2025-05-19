import task_management as tm
import task_editing as te
import task_tracking as tt

tm1 = tm.TaskManagement()
def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Track Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            tm1.add_task(tm)
        elif choice == '2':
            te.edit_task(tm)
        elif choice == '3':
            tt.track_task(tm)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")