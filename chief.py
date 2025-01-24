from datetime import datetime
from task import PersonalTask, WorkTask
from task_management import TaskManagement
from task_editing import TaskEditing
from task_tracking import TaskTracking


def menu():
    management = TaskManagement()
    edit = TaskEditing(management)
    track = TaskTracking(management)

    while True:
        print("\nPlease choose an option:")
        print("1. Add Personal Task")
        print("2. Add Work Task")
        print("3. Display All Tasks")
        # task management
        print("4. Edit Task Status")
        print("5. Set Task Priority")
        print("6. Edit Task Deadline")
        print("7. Mark Task as Completed")
        # task editing
        print("8. Get Task Color")
        print("9. Get Task Status")
        print("10. Get Task Deadline")
        # task tracking
        print("11. Exit")
        
        try:
            choice = int(input("\nplease enter your choice (1-11): "))
            if not 0 < choice < 12:
                print("invalid input please enter a number between 1 and 11")
                continue

            if choice == 1:
                task_name = input("please enter the personel task name: ")
                while True:
                    try:
                        task_id = int(input("please enter task id: "))
                        deadline = input("enter deadline (YYYY-MM-DD): ")
                        datetime.strptime(deadline, "%Y-%m-%d")
                        break  
                    except ValueError:
                        print("invalid date format please enter the valid format => YYYY-MM-DD!")
                
                p1 = PersonalTask(task_id, task_name, deadline)
                management.add_task(p1)
                print("personal task added successfully!!")

            elif choice == 2:
                task_name = input("enter the work task name: ")
                while True:
                    try:
                        task_id = int(input("enter task id: "))
                        deadline = input("enter deadline (YYYY-MM-DD): ")
                        datetime.strptime(deadline, "%Y-%m-%d")
                        break  
                    except ValueError:
                        print("invalid date format please enter the valid format => YYYY-MM-DD!")
                
                w1 = WorkTask(task_id, task_name, deadline)
                management.add_task(w1)
                print("work task added successfully.")

            elif choice == 3:
                management.display_tasks()

            elif choice == 4: # task edit ----------------------------------
                if management.task_list:
                    status = input("enter a new status : ")
                    while True:
                        try:
                            task_id = int(input("enter task id to edit status: "))
                            break
                        except ValueError:
                            print("invalid input please enter a valid task id")
                        valueStatus = edit.set_task_status(task_id, status)

                        if valueStatus == None:
                            print("id not found!")
                        else:
                            print(f"task {task_id} status updated to {status}")
                else:
                    print("there is no task to edit")

            

            elif choice == 5:
                if management.task_list:
                    while True:
                        try:
                            task_id = int(input("enter task id to set priority: "))
                            priority = input("enter priority (low, medium, high): ")
                            break
                        except ValueError:
                            print("invalid input please enter a valid task id")
                        valuePriority = edit.set_prioritization(task_id, priority)
                        if valuePriority == None:
                            print("id not found!")
                        else:
                            print(f"Task {task_id} priority updated to {priority}.")
                else:
                    print("there  is no task to edit")

                   
            elif choice == 6:
                if management.task_list:
                        
                    while True:
                        try:
                            task_id = int(input("enter task id to edit deadline: "))
                            deadline = input("enter new deadline (YYYY-MM-DD): ")
                            datetime.strptime(deadline, "%Y-%m-%d")
                            break
                        except ValueError:
                            print("invalid date format please enter the valid format => YYYY-MM-DD!")


                        valueDeadline = edit.set_new_date(task_id, deadline)
                        if valueDeadline == None:
                            print("id not found!")
                        else:
                            print(f"Task {task_id} deadline updated to {deadline}.")
                else:  
                    print("there is no task to edit")          
                    
                
            elif choice == 7:
                if management.task_list:
                    while True:
                        try:
                            task_id = int(input("enter task i to mark as completed: "))
                            break
                        except ValueError:
                            print("invalid input please enter a valid task id")
                        valueMark = edit.mark_status_completed(task_id)
                        if valueMark == None:
                            print("id not found")
                        else:
                            print(f"task {task_id} marked as completed..")
                else:
                    print("there is no task to edit")


            elif choice == 8: # task tracking
                if management.task_list:
                    while True:
                        try:
                            task_id = int(input("enter task id to get color: "))
                            break
                        except ValueError:
                            print("invalid input. Please enter a valid task id")
                        valueColor = track.get_task_color(task_id)
                        if valueColor == None:    
                            print("id con not found")
                        else:
                            print(f"task {task_id} color is {valueColor}.")
                else:
                    print("there is no task to get color")

                


            
            elif choice == 9:
                if management.task_list:
                    while True:
                        try:
                            task_id = int(input("enter task id to get status: "))
                            break
                        except ValueError:
                            print("invalid input please enter a valid task id")
                        valueStatus = track.get_task_status(task_id)
                        if valueStatus == None:
                            print("id not found")
                        else:
                            print(f"task {task_id} status is {status}.")
                else:
                    print("there is no task to get status")



            elif choice == 10:
                if management.task_list:
                    while True:
                        try:
                            task_id = int(input("enter task id to get deadline: "))
                            break
                        except ValueError:
                            print("invalid input please enter a valid task id.")
                        valueDeadline = track.get_task_deadline(task_id)
                        if deadline == None:
                            print("id not found")
                        else:
                            print(f"task {task_id} deadline is {deadline}.")
                else:
                    print("there is no ask to get deadline")    
            
            elif choice == 11:
                print("exiting the menu.")
                break

        except ValueError:
            print("invalid input please enter a number between 1 and 11.")



if __name__ == "__main__":
    menu()
