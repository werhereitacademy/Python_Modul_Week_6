import os
from typing import Any, Dict, List, Optional, Union

def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    
def show_message(message: str) -> None:
    """
    Display a status message and wait for user input to continue.

    Args:
        message (str): The message to be displayed.
    """
    print(message)
    input("\nPress any key to continue...")

def get_choice(options: Union[List[str], Dict[str, Any]]) -> str:
    """
    Prompt the user to input a choice from the available options.

    Args:
        options (list or dict): A list or dictionary of valid choices.

    Returns:
        str: The valid choice entered by the user.
    """
    while True:
        try:
            choice = input("Your choice: ").strip()
            if choice in options:
                return choice
            else:
                raise ValueError
        except ValueError:
            print("⚠️  Please enter a valid number.")

def print_centered_colored_line(menu_name: str, width: int = 30, color_code: str = "\033[1;33m") -> None:
    """
    Print a centered colored line for menu titles with given width.

    Args:
        menu_name (str): The text to display centered.
        width (int, optional): Total width of the line including padding. Defaults to 30.
        color_code (str, optional): ANSI color escape code. Defaults to yellow bold.
    """
    reset_code = "\033[0m"
    
    # Center the text excluding color codes
    text = menu_name.center(width - 2)
    
    # Apply color codes
    colored_text = f"{color_code}{text}{reset_code}"
    
    # Print the colored centered text
    print(colored_text)            

def header(menu_name: str, menu_width: int = 30) -> None:
    """
    Clear the screen and display a stylized menu header.

    Args:
        menu_name (str): The menu title to display.
        menu_width (int, optional): Width of the menu header. Defaults to 30.
    """
    clear_screen()
    print()
    print_centered_colored_line(menu_name, menu_width)
    print('-' * menu_width)

def show_list(title: str, column_names: List[str], list_items: List[Any]) -> None:
    """
    Display a formatted list with colored rows and headers.

    Args:
        title (str): Title of the list/menu.
        column_names (list): List of column header names.
        list_items (list): List of objects/items to display. 
            Each item should have attributes: task_id, task_name, deadline, status, priority, and color.
    """
    # ANSI color codes
    color_map = {
        "Blue": "\033[94m",
        "Geel": "\033[93m",
        "Red": "\033[91m",
        "Green": "\033[92m",
        "Reset": "\033[0m"
    }

    # Column widths predefined for formatting
    col_widths = [6, 25, 12, 14, 12]

    # Build and print the header row
    header_row = '| ' + '| '.join(name.center(col_widths[i]) for i, name in enumerate(column_names)) + ' |'
    menu_width = len(header_row) + 5  # Additional space for borders
    header(title, menu_width)
    print(header_row)
    print('-' * menu_width)

    # Print each item row with colors
    for i, item in enumerate(list_items, start=1):
        if hasattr(item, '__dict__'):
            values = [
                str(item.task_id),
                str(item.task_name),
                str(item.deadline),
                str(item.status),
                str(item.priority),
            ]
            # Get color code based on item's color attribute
            color_code = color_map.get(item.color, "")
            reset = color_map["Reset"]

            # Format each column with color inside borders
            colored_row = '| ' + ' | '.join(
                f"{color_code}{values[i].ljust(col_widths[i])}{reset}" for i in range(len(values))
            ) + '  |'
            print(colored_row)

    print('-' * menu_width)

def show_menu(title: str, options: Dict[str, str], width: int = 30) -> str:
    """
    Display a menu with a header and options, then get a valid user choice.

    Args:
        title (str): The menu title.
        options (dict): Dictionary of option keys and their descriptions.
        width (int, optional): The width of the menu display. Defaults to 30.

    Returns:
        str: The key selected by the user.
    """
    header(title, width)
    for key, val in options.items():
        print('|' + ' ' * 4 + f"   {key} - {val}".ljust(width - 6) + '|')
    print('-' * width)
    return get_choice(options.keys())

def show_options(title: str, options: Dict[str, str]) -> str:
    """
    Display options in a simple list format and return the selected value.

    Args:
        title (str): The title describing the option set.
        options (dict): Dictionary of option keys and values.

    Returns:
        str: The value corresponding to the selected key.
    """
    print(f"\n🔹 {title}")
    for key, val in options.items():
        print(f"   {key}: {val}")
    return options[get_choice(options)]

def display_main_menu() -> str:
    """
    Display the main menu of the Task Management System.

    Returns:
        str: The option selected by the user.
    """
    return show_menu("Task Management System", {
        "1": "Show Tasks",
        "2": "Add Task",
        "3": "Edit Task",
        "0": "Exit"
    })

def task_editing_menu() -> str:
    """
    Display the sub-menu for task editing options.

    Returns:
        str: The option selected by the user.
    """
    return show_menu("Task Editing Menu", {
        "1": "Set Task Status",
        "2": "Set Priority",
        "3": "Set New Deadline",
        "4": "Mark Task as Completed",
        "0": "Exit"
    })
