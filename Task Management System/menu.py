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
    print_centered_colored_line(menu_name, 30)
    print('-' * menu_width)

def show_list(title, column_names, list_items, width=100):
    header(title, width)

    # Sütun genişlikleri (manuel olarak ayarlanabilir veya otomatik yapılabilir)
    col_widths = [6, 20, 14, 14, 10, 10]  # toplam: ~74 + boşluklar = 100 içinde rahat

    # Başlıkları hizalı yazdır
    header_row = '| ' + ' | '.join(name.ljust(col_widths[i]) for i, name in enumerate(column_names)) + ' |'
    print('-' * len(header_row))
    print(header_row)
    print('-' * len(header_row))

    # Satırları hizalı yazdır
    for i, item in enumerate(list_items, start=1):
        if hasattr(item, '__dict__'):
            values = [
                str(item.task_id),
                str(item.task_name),
                str(item.deadline),
                str(item.status),
                str(item.priority),
                str(item.color)
            ]
            row = '| ' + ' | '.join(values[i].ljust(col_widths[i]) for i in range(len(values))) + ' |'
            print(row)
        else:
            print(f"| {str(i).ljust(width - 4)} |")  # fallback

    print('-' * len(header_row))


# General-purpose menu display function
def show_menu(title, options, width=30):
    header(title, width)
    for key, val in options.items():
        print('|' + ' ' * 5 + f"   {key} - {val}".ljust(width - 7) + '|')
    print('-' * width)
    return get_choice(options.keys())

# Ensures a valid numeric input is selected from options
def show_options(title, options):
    print(f"\n🔹 {title}")
    for key, val in options.items():
        print(f"   {key}: {val}")
    return get_choice(options)

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

