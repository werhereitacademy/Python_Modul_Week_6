import tkinter as tk
from ui.app_ui import TaskApp

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
    # root.geometry("800x600")
    # root.title("Task Manager")
    # root.configure(bg="lightblue")