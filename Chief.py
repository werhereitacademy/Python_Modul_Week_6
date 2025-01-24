from task_management import TaskManagement
from task_editing import TaskEditing
from task_tracking import TaskTracking
from Tasks import WorkTask, PersonalTask

# Initialize TaskManagement
tm = TaskManagement()

# Create WorkTask and PersonalTask
p1 = PersonalTask("1", "Task1", "12/12/2021")
p2 = PersonalTask("2", "Task2", "12/12/2021")   
w1 = WorkTask("3", "Task3", "12/12/2021")
w2 = WorkTask("4", "Task4", "12/12/2021")

#Color your task
p1.color_your_task()
w1.color_your_task()

# Add tasks to TaskManagement
tm.add_task(p1)
tm.add_task(w1)

# Display all tasks
print("Initial Tasks:")
tm.display_task()

# Edit tasks using TaskEditing
te = TaskEditing(tm)
te.set_task_status("1", "In Progress")
te.set_prioritization("3", "Medium")


# Display updated tasks
print("\nUpdated Tasks:")
tm.display_task()

# Track tasks using TaskTracking
tt = TaskTracking(tm)
print("\nTask Tracking for Task ID 1:")
tt.get_task_status("1")
tt.get_task_deadline("1")
tt.get_task_color("1")

print("\nTask Tracking for Task ID 31:")
tt.get_task_status("3")
tt.get_task_deadline("3")
tt.get_task_color("3")
