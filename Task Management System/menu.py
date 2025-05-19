import os

clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')


# Süreclerle ilgili durum bildirimi
def show_message(message):
    print(message)
    input("\nDevam etmek için bir tuşa basın...")

def header(menu_name, menu_width=30):
    clear_screen()
    print('-' * menu_width)
    print('|' + f"\033[1;33m"+ menu_name.center(menu_width - 2)+f"\033[0m" + '|')
    print('-' * menu_width)

def display_menu(title, options, width=30):
    header(title, width)
    for option in options:
        print('|' + ' ' * 8 + option.ljust(width - 10) + '|')
    print('-' * width)

def display_main_menu():
    main_menu = [
        "1. Add Task",
        "2. Edit Task",
        "3. Track Task",
        "0. Exit"
    ]

    display_menu("Task Management System", main_menu)

def task_editing_menu():    
    edit_menu = [
        "1 - Set Task Status",
        "2 - Set Priority",
        "3 - Set New Deadline",
        "4 - Set Task as Completed",
        "0 - Exit"
    ]

    display_menu("ÜYELİK İŞLEMLERİ", edit_menu)     