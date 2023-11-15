import tkinter as tk

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks.pop(task_index - 1)
            task.completed = True
            self.completed_tasks.append(task)

    def update_task(self, task_index, description, due_date, priority):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.description = description
            task.due_date = due_date
            task.priority = priority

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks.pop(task_index - 1)

# Create a Tkinter GUI

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.to_do_list = ToDoList()

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.pack()

        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.due_date_label = tk.Label(root, text="Due Date:")
        self.due_date_label.pack()

        self.due_date_entry = tk.Entry(root)
        self.due_date_entry.pack()

        self.priority_label = tk.Label(root, text="Priority:")
        self.priority_label.pack()

        self.priority_entry = tk.Entry(root)
        self.priority_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.display_button = tk.Button(root, text="Display Tasks", command=self.display_tasks)
        self.display_button.pack()

        self.mark_completed_button = tk.Button(root, text="Mark Task as Completed", command=self.mark_task_completed)
        self.mark_completed_button.pack()

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()

    def add_task(self):
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()
        self.to_do_list.add_task(description, due_date, priority)
        self.clear_entries()

    def display_tasks(self):
        task_window = tk.Toplevel(self.root)
        task_window.title("Tasks")

        task_text = tk.Text(task_window)
        task_text.pack()

        task_text.insert(tk.END, "To-Do List:\n")
        for index, task in enumerate(self.to_do_list.tasks, start=1):
            task_text.insert(tk.END, f"{index}. {task.description} (Due: {task.due_date}, Priority: {task.priority})\n")

        task_text.insert(tk.END, "\nCompleted Tasks:\n")
        for index, task in enumerate(self.to_do_list.completed_tasks, start=1):
            task_text.insert(tk.END, f"{index}. {task.description} (Due: {task.due_date}, Priority: {task.priority})\n")

    def mark_task_completed(self):
        task_window = tk.Toplevel(self.root)
        task_window.title("Mark Task as Completed")

        task_text = tk.Text(task_window)
        task_text.pack()

        task_text.insert(tk.END, "To-Do List:\n")
        for index, task in enumerate(self.to_do_list.tasks, start=1):
            task_text.insert(tk.END, f"{index}. {task.description} (Due: {task.due_date}, Priority: {task.priority})\n")

        task_index = int(input("Enter the index of the task to mark as completed: "))
        self.to_do_list.mark_task_completed(task_index)

    def update_task(self):
        task_index = int(input("Enter the index of the task to update: "))
        description = input("Enter new description: ")
        due_date = input("Enter new due date (optional): ")
        priority = input("Enter new priority (low, medium, high): ")
        self.to_do_list.update_task(task_index, description, due_date, priority)

    def remove_task(self):
        task_index = int(input("Enter the index of the task to remove: "))
        self.to_do_list.remove_task(task_index)

    def clear_entries(self):
        self.description_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
