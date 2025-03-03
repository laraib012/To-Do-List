import tkinter as tk
from task_management import TaskManagement
from filehandling import FileHandler

def main():
    root = tk.Tk()
    
    # Initialize task management
    task_manager = TaskManagement(root)
    
    # Initialize file handler
    file_handler = FileHandler(task_manager, root)
    
    # Load tasks on startup
    file_handler.load_on_startup()
    
    root.mainloop()

if __name__ == "__main__":
    main()