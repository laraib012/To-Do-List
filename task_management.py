import tkinter as tk
from tkinter import messagebox

class TaskManagement:
    def __init__(self, root):
        self.root = root
        self.tasks = []
        self.setup_ui()
        
    def setup_ui(self):
        # Set window properties
        self.root.title("To-Do List Application")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")
        
        # Create header for to do list
        header_frame = tk.Frame(self.root, bg="#4a6572")
        header_frame.pack(fill=tk.X)
        
        header_label = tk.Label(
            header_frame, 
            text="TO-DO LIST", 
            font=("Arial", 16, "bold"), 
            bg="#4a6572", 
            fg="white",
            pady=10
        )
        header_label.pack()
        
        # Create task entry area
        entry_frame = tk.Frame(self.root, bg="#f5f5f5", pady=10)
        entry_frame.pack(fill=tk.X, padx=20)
        
        self.task_entry = tk.Entry(
            entry_frame, 
            width=30, 
            font=("Arial", 12),
            bd=2,
            relief=tk.GROOVE
        )
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.focus_set()
        
        # Create Add Task button
        add_button = tk.Button(
            entry_frame, 
            text="Add Task",
            font=("Arial", 10, "bold"),
            bg="#344955",
            fg="white",
            padx=10,
            command=self.add_task
        )
        add_button.pack(side=tk.LEFT, padx=5)
        
        # Create Remove Task button
        remove_button = tk.Button(
            entry_frame, 
            text="Remove Task",
            font=("Arial", 10, "bold"),
            bg="#d32f2f",
            fg="white",
            padx=10,
            command=self.remove_task
        )
        remove_button.pack(side=tk.LEFT, padx=5)
        
        # Create list of tasks
        list_frame = tk.Frame(self.root, bg="white", bd=2, relief=tk.GROOVE)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.task_listbox = tk.Listbox(
            list_frame,
            font=("Arial", 12),
            selectbackground="#a6bbc8",
            selectmode=tk.SINGLE,
            bd=0,
            width=0,
            height=0
        )
        self.task_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add scrollbar
        scrollbar = tk.Scrollbar(self.task_listbox)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("0 tasks pending")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Arial", 10),
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg="#f5f5f5"
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.update_status()
            return True
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
            return False
            
    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index)
            self.update_status()
            return True
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove!")
            return False
    
    def update_status(self):
        count = len(self.tasks)
        task_text = "task" if count == 1 else "tasks"
        self.status_var.set(f"{count} {task_text} pending")
    
    def get_tasks(self):
        return self.tasks
    
    def set_tasks(self, tasks):
        self.tasks = tasks
        self.task_listbox.delete(0, tk.END)
        for task in tasks:
            self.task_listbox.insert(tk.END, task)
        self.update_status()

# For testing this module independently
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagement(root)
    root.mainloop()