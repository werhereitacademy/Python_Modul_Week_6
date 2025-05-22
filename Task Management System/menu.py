import os

clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Display a status message for ongoing processes
def show_message(message):
    print(message)
    input("\nPress any key to continue...")

def get_choice(options):
    while True:
        try:
            choice = input("Your choice: ").strip()
            if choice in options:
                return choice
            else:
                raise ValueError
        except ValueError:
            print("⚠️  Please enter a valid number.")

def print_centered_colored_line(menu_name, width=30, color_code="\033[1;33m"):
    reset_code = "\033[0m"
    
    # Yazı genişliğini renk kodları hariç olacak şekilde ortala
    text = menu_name.center(width - 2)
    
    # Renkli hale getir (ortalanmış yazıya uygula)
    colored_text = f"{color_code}{text}{reset_code}"
    
    # Kenarlara çerçeve çizgileri ekle
    print(colored_text)            

# Prints a stylized menu header
def header(menu_name, menu_width=30):
    clear_screen()
    print()
    print_centered_colored_line(menu_name, menu_width)
    print('-' * menu_width)

def show_list(title, column_names, list_items):
    # ANSI color codes
    color_map = {
        "Blue": "\033[94m",
        "Geel": "\033[93m",
        "Red": "\033[91m",
        "Green": "\033[92m",
        "Reset": "\033[0m"
    }

    # Column widths
    col_widths = [6, 25, 12, 14, 12]

    # Build and print the header
    header_row = '| ' + '| '.join(name.center(col_widths[i]) for i, name in enumerate(column_names)) + ' |'
    menu_width = len(header_row) + 5  # 5 for the borders
    header(title, menu_width)
    print(header_row)
    print('-' * menu_width)

    # Print each task row
    for i, item in enumerate(list_items, start=1):
        if hasattr(item, '__dict__'):
            values = [
                str(item.task_id),
                str(item.task_name),
                str(item.deadline),
                str(item.status),
                str(item.priority),
            ]
            # Color only the content between the borders
            color_code = color_map.get(item.color, "")
            reset = color_map["Reset"]

            colored_row = '| ' + ' | '.join(
                f"{color_code}{values[i].ljust(col_widths[i])}{reset}" for i in range(len(values))
            ) + '  |'
            print(colored_row)

    print('-' * menu_width)

# General-purpose menu display function
def show_menu(title, options, width=30):
    header(title, width)
    for key, val in options.items():
        print('|' + ' ' * 4 + f"   {key} - {val}".ljust(width - 6) + '|')
    print('-' * width)
    return get_choice(options.keys())

# Ensures a valid numeric input is selected from options
def show_options(title, options):
    print(f"\n🔹 {title}")
    for key, val in options.items():
        print(f"   {key}: {val}")
    return options[get_choice(options)]

# Main menu display function
def display_main_menu():
    return show_menu("Task Management System", {
        "1": "Show Tasks",
        "2": "Add Task",
        "3": "Edit Task",
        "0": "Exit"
    })

# Task editing sub-menu
def task_editing_menu():
    return show_menu("Task Editing Menu", {
        "1": "Set Task Status",
        "2": "Set Priority",
        "3": "Set New Deadline",
        "4": "Mark Task as Completed",
        "0": "Exit"
    })

