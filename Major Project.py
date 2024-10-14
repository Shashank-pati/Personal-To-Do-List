import tkinter as tk
from tkinter import messagebox
import csv

#Creating a class
class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal To-Do List Manager")
        self.tasks = self.load_tasks()

        # Creating Frames for Layout
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack()
        self.frame4 = tk.Frame(self.root)
        self.frame4.pack()

        # Creating Labels and Entring fields for tasks
        tk.Label(self.frame1, text="Title : ").pack(side=tk.LEFT)
        self.title_entry = tk.Entry(self.frame1)
        self.title_entry.pack(side=tk.LEFT)
        tk.Label(self.frame1, text="Description : ").pack(side=tk.LEFT)
        self.description_entry = tk.Entry(self.frame1)
        self.description_entry.pack(side=tk.LEFT)
        tk.Label(self.frame1, text="Category : ").pack(side=tk.LEFT)
        self.category_entry = tk.Entry(self.frame1)
        self.category_entry.pack(side=tk.LEFT)
        tk.Label(self.frame4, text="View Task by Title:").pack(side=tk.LEFT)
        self.view_title_entry = tk.Entry(self.frame4)
        self.view_title_entry.pack(side=tk.LEFT)

        # Creating Buttons for managemnt of task
        tk.Button(self.frame2, text="Add New Task", command=self.add).pack(side=tk.LEFT)
        tk.Button(self.frame2, text="Mark as Completed", command=self.completed).pack(side=tk.LEFT)
        tk.Button(self.frame2, text="Delete Selected Task", command=self.delete).pack(side=tk.LEFT)
        tk.Button(self.frame4, text="View Task", command=self.view).pack(side=tk.LEFT)

        # Creating a listbox for displaying the task
        self.listbox = tk.Listbox(self.frame3)
        self.listbox.pack()
        self.update()

        # Creating a Instruction label for easy accessiblity to user
        tk.Label(self.root, text="Instructions :\n\nEnter task Details and click 'Add Task' to add a task.\nSelect the task and click on 'Mark as Completed' to mark it as completed.\nSelect a task and click on 'Delete Task' to delete it.\nEnter the Title to view the Details of the Task").pack()
 
                
        # Create label to display task details
        self.task_details_label = tk.Label(self.root, text="", wraplength=400)
        self.task_details_label.pack()

    def load_tasks(self):  #Function to Load tasks from CSV file
        try:  #Using try to except Error in case the file is not present there 
            with open('tasks.csv', 'r') as file:
                reader = csv.reader(file)
                tasks = list(reader)
                return tasks
        except FileNotFoundError:
            return []
        
    #Saving the tasks to a CSV file
    def save_tasks(self):
        with open('tasks.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.tasks)

    #Adding a new task to the List    
    def add(self):
        t = self.title_entry.get()
        desc = self.description_entry.get()
        c = self.category_entry.get()
        if t and desc and c:
            self.tasks.append([t, desc, c, 'Not Completed'])
            self.save_tasks()
            self.update()
            self.title_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill the necessary details in all fields provided.")


    #Marking the selected task as completed entered into the list
    def completed(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks[index][3] = 'Completed'
            self.save_tasks()
            self.update()
        except IndexError:
            messagebox.showerror("Error", "Select a task to mark as completed.")


    #Deleting the selected task from the entered list
    def delete(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            self.save_tasks()
            self.update()
        except IndexError:
            messagebox.showerror("Error", "Please, Select a task to delete.")


    #Viewing the Details of a task by entering its title
    def view(self):
        title = self.view_title_entry.get()
        for task in self.tasks:
            if task[0] == title:
                details = f"Title : {task[0]}\nDescription: {task[1]}\nCategory: {task[2]}\nStatus: {task[3]}"
                self.task_details_label.config(text=details)
                return
        messagebox.showerror("Error", "The mentioned Task not found.")


    #Updating the Listbox to Display the current tasks
    def update(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, f"Title: {task[0]}, Description: {task[1]}, Category: {task[2]}, Status: {task[3]}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()