"""
CLI To-Do List App 
------------------
A simple command-line tool to manage your daily tasks.
Features:
- Add tasks
- View all tasks
- Mark tasks as completed
- Delete tasks

Author: Elvin James
Date: 2025-08-02
"""

tasks = {}  # Empty dictionary

def add_task():
    task = input("Add a task:\n")
    task_id = len(tasks) + 1  # Simple ID system
    tasks[task_id] = task
    print(f"Task {task_id} added!")
    main()

def view_task():
    if not tasks:
        print("No tasks yet.")
    else:
        for task_id, task in tasks.items():
            print(f"{task_id}: {task}")
    main()

def mark_task():
    task_id = int(input("Enter task ID to mark as done: "))
    if task_id in tasks:
        tasks[task_id] += " ✅"
        print(f"Task {task_id} marked as done!")
    else:
        print("Task not found.")
    main()

def del_task():
    task_id = int(input("Enter task ID to delete: "))
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task {task_id} deleted!")
    else:
        print("Task not found.")
    main()

def main():
    print("""--------------------
Commands:
  1. Add a new task
  2. View all tasks
  3. Mark a task as done
  4. Delete a task
  5. Exit""")
    
    choice = int(input("Select an Option [1-5]: "))
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        mark_task()
    elif choice == 4:
        del_task()
    elif choice == 5:
        quit("""==========================================\nThanks for using CLI To-Do List Application\n==========================================\n Developed with ❤️   by Elvin
             """)
    
    else:
        print("Please Enter a valid number")
        
print("""==================================
 Welcome to Your CLI To-Do List 📝
==================================
Easily keep track of your tasks right from the terminal.""")
main()