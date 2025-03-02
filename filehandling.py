import json
import os
import tkinter as tk
from tkinter import messagebox, filedialog

class FileHandler:
    def __init__(self, task_manager, root):
        self.task_manager = task_manager
        self.root = root
        self.default_filename = "tasks.json"
        self.setup_ui()
        
    def setup_ui(self):
        # Create buttons frame
        button_frame = tk.Frame(self.root, bg="#f5f5f5", pady=10)
        button_frame.pack(fill=tk.X, padx=20)
        
        # Create Save button
        save_button = tk.Button(
            button_frame,
            text="Save Tasks",
            font=("Arial", 10, "bold"),
            bg="#4caf50",
            fg="white",
            padx=10,
            command=self.save_tasks
        )
        save_button.pack(side=tk.LEFT, padx=5)
        
        # Create Load button
        load_button = tk.Button(
            button_frame,
            text="Load Tasks",
            font=("Arial", 10, "bold"),
            bg="#2196f3",
            fg="white",
            padx=10,
            command=self.load_tasks
        )
        load_button.pack(side=tk.LEFT, padx=5)
        
        # Create Clear All button
        clear_button = tk.Button(
            button_frame,
            text="Clear All",
            font=("Arial", 10, "bold"),
            bg="#ff9800",
            fg="white",
            padx=10,
            command=self.clear_tasks
        )
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Create custom save button
        custom_save_button = tk.Button(
            button_frame,
            text="Save As...",
            font=("Arial", 10, "bold"),
            bg="#607d8b",
            fg="white",
            padx=10,
            command=self.save_tasks_as
        )
        custom_save_button.pack(side=tk.LEFT, padx=5)
    
    def save_tasks(self):
        tasks = self.task_manager.get_tasks()
        try:
            with open(self.default_filename, 'w') as file:
                json.dump(tasks, file)
            messagebox.showinfo("Success", f"Tasks saved to {self.default_filename}")
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Could not save tasks: {str(e)}")
            return False
    
    def save_tasks_as(self):
        tasks = self.task_manager.get_tasks()
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w') as file:
                    json.dump(tasks, file)
                messagebox.showinfo("Success", f"Tasks saved to {filename}")
                return True
            except Exception as e:
                messagebox.showerror("Error", f"Could not save tasks: {str(e)}")
                return False
        return False
    
    def load_tasks(self, filename=None):
        if filename is None:
            filename = self.default_filename
            
            # Check if default file doesn't exist, offer to browse
            if not os.path.exists(filename):
                response = messagebox.askyesno(
                    "File Not Found", 
                    f"{filename} doesn't exist. Would you like to select a different file?"
                )
                if response:
                    filename = filedialog.askopenfilename(
                        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
                    )
                    if not filename:
                        return False
                else:
                    return False
        
        try:
            with open(filename, 'r') as file:
                tasks = json.load(file)
            
            self.task_manager.set_tasks(tasks)
            messagebox.showinfo("Success", f"Tasks loaded from {filename}")
            return True
        except FileNotFoundError:
            messagebox.showerror("Error", f"File {filename} not found")
            return False
        except json.JSONDecodeError:
            messagebox.showerror("Error", f"File {filename} is not a valid JSON file")
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Could not load tasks: {str(e)}")
            return False
    
    def clear_tasks(self):
        response = messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?")
        if response:
            self.task_manager.set_tasks([])
            messagebox.showinfo("Success", "All tasks cleared")
            return True
        return False
    
    def load_on_startup(self):
        # Silently try to load tasks on startup, don't show error if file doesn't exist
        if os.path.exists(self.default_filename):
            try:
                with open(self.default_filename, 'r') as file:
                    tasks = json.load(file)
                self.task_manager.set_tasks(tasks)
                return True
            except:
                return False
        return False