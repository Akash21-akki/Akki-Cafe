tasks = []

def add_Task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_Task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{tasks}' remove!")
    else:
        print("Task not found!")

def view_Task():
    if not tasks:
        print("No tasks added yet!")
    else:
        print("\nYour Tasks")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}, {task}")

while True:
    print("\n1. Add Task\n2. Remove Task\n3. View Task\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter Task: ")
        add_Task(task)

    elif choice == '2':
        task = input("Enter task to remove: ")
        remove_Task(task)
    
    elif choice == '3':
        view_Task()
    
    elif choice == '4':
        print("Exiting...Goodbye!")
        break

    else:
        print("Invalid choice! Try again")