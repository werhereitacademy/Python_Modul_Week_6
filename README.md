# Python_Modul_Week_6

# TASK I

![image](https://github.com/user-attachments/assets/0c278632-b9fc-4a53-9d84-e87b007abf02)




#### Overview
This Python program is a simple Task Management System that allows users to create, edit, track, and display tasks. It uses Object-Oriented Programming (OOP) principles to create a structured system for managing tasks.
##### Prerequisites
Before working on this program, students should have a basic understanding of the following concepts:
1. Python programming fundamentals (variables, functions, classes, objects).
2. Inheritance and abstract classes in Python.
3. Working with dates and times in Python (using the datetime module).
4. Exception handling in Python.
5. Basic knowledge of interfaces/abstract classes (Python ABC).
### Program Structure
1. **Task Management Class (`TaskManagement`)**
  This class serves as the core component of the task management system.
  - It maintains a list (`task_list`) to store all task objects.
  - It provides methods to add new tasks and display the list of existing tasks.
2. **Task Scheduling (Handled via instantiating `PersonalTask` or `WorkTask`)**
  While not represented by a separate class in the code, task creation and classification are performed by instantiating `PersonalTask` and `WorkTask`.
  - These objects are then added to `TaskManagement`.
  - It ensures appropriate task typing by using inheritance.
3. **Task Editing Class (`TaskEditing`)**
  This class enables various edit operations on existing tasks.
  - Students learn how to modify task attributes such as `status`, `priority`, and `deadline`.
  - It also demonstrates how to find tasks by ID and update their attributes.
4. **Task Tracking Class (`TaskTracking`)**
  This class allows for tracking the state and metadata of tasks.
  - Students can retrieve task status, deadline, and color by task ID.
  - It provides read-only access to key attributes.
5. **Abstract Base Class (`Task`)**
  Defines the common structure and behavior for all task types.
  - Includes attributes such as `task_id`, `task_name`, `deadline`, `status`, `priority`, and `color`.
  - Contains a method to calculate the number of days left until the deadline.
  - Declares an abstract method `color_your_task()` to be implemented by subclasses.
6. **Subclasses (`PersonalTask` and `WorkTask`)**
  These classes inherit from `Task` and define behavior specific to personal and work-related tasks.
  - They implement the `color_your_task()` method to assign different colors.
  - Default priorities are also handled here (e.g., `Low` for personal, `High` for work).
  - Demonstrates inheritance and method overriding.
7. **Special Keywords Dictionary (`SPECIAL_KEYWORDS`)**
  A global dictionary maps strings like `"today"`, `"tomorrow"`, and `"next week"` to actual dates using `datetime`.
  - Teaches students about dictionary usage and date manipulation in Python.
---
### Key Learning Points
- Core Object-Oriented Programming concepts: classes, objects, inheritance, and abstract base classes.
- Proper encapsulation and separation of concerns (management, editing, and tracking are decoupled).
- Exception handling and task lookup strategies.
- Working with date and time using Python’s `datetime` module.
- Using dictionaries for keyword mapping and processing.
- Implementing and overriding abstract methods in subclasses.
---
### Assignment Ideas for Students
- Create a new task type (e.g., `StudyTask`) that inherits from `Task` and implements custom behavior and attributes.
- Extend the editing functionality to include features like setting a task note or changing the color manually.
- Add the ability to sort tasks by priority or deadline.
- Develop a simple command-line interface (CLI) or GUI to interact with the task manager.
- Write unit tests to verify that core functionalities (adding, editing, tracking) work as expected.
> By working on these exercises, students will strengthen their understanding of OOP principles and improve their Python software development skills.

##### Exp: Let's consider an example where we create, edit, and track tasks using your program:
![image (2)](https://github.com/user-attachments/assets/7b70b1c1-3e67-4bf6-9629-e4badab118d3)


##### Expected Output:
![{63AE01CD-833A-4229-974B-D9E4E8BA5AFA}](https://github.com/user-attachments/assets/74bcc5db-cc04-4c99-8ca1-c9996d03c5fe)


# TASK II

### Below, you will find screenshots of Python class code for a Note application. Carefully examine the code and draw a UML (Unified Modeling Language) class diagram according to the following instructions:
1.     Indicate the name of each class.
2.     List the attributes (fields) and methods of each class.
3.     Show the relationships between classes correctly.
4.     If applicable, indicate collections like List<Note> explicitly in your diagram

![image](https://github.com/user-attachments/assets/2bfeab3b-8d1e-4430-9019-c5501c99f758)
![image](https://github.com/user-attachments/assets/3e019171-9b4b-48d0-8bfb-93caf4dd173d)
![image](https://github.com/user-attachments/assets/12635427-2e96-4c2a-8137-2dee113a1058)



## Hackerrank Questions

1. sWAP cASE: https://www.hackerrank.com/challenges/swap-case/problem

2. String Split and Join: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

3. Mutations: https://www.hackerrank.com/challenges/python-mutations/problem

4. Text Wrap: https://www.hackerrank.com/challenges/text-wrap/problem


Ali: task.py
Furkan: task_management
Mustfa: task_tracking
Lütfü: task_editing