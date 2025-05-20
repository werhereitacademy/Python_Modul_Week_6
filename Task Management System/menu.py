import os

clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')


# Display a status message for ongoing processes
def show_message(message):
    print(message)
    input("\nPress any key to continue...")

# Ensures a valid numeric input is selected from options
def show_options(title, options):
    print(f"\n🔹 {title}")
    for key, val in options.items():
        print(f"   {key}: {val}")
    return options[get_choice(options)]

def get_choice(options):
    while True:
        try:
            choice = input("Your choice: ").strip()
            if choice in options:
                return choice
            else:
                print("⚠️ Invalid selection. Please try again.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

# Prints a stylized menu header
def header(menu_name, menu_width=30):
    clear_screen()
    print('-' * menu_width)
    print('|' + f"\033[1;33m" + menu_name.center(menu_width - 2) + f"\033[0m" + '|')
    print('-' * menu_width)

# General-purpose menu display function
def show_menu(title, options, width=30):
    header(title, width)
    for option in options.values():
        print('|' + ' ' * 8 + option.ljust(width - 10) + '|')
    print('-' * width)

# Main menu display function
def display_main_menu():
    show_menu("Task Management System", {
        "1": "Add Task",
        "2": "Edit Task",
        "3": "Track Task",
        "0": "Exit"
    })
    return int(input("Select an option: ").strip())

# Task editing sub-menu
def task_editing_menu():
    show_menu("Task Editing Menu", {
        "1": "Set Task Status",
        "2": "Set Priority",
        "3": "Set New Deadline",
        "4": "Mark Task as Completed",
        "0": "Exit"
    })
    return int(input("Select an option: ").strip())
