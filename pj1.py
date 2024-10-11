class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks[task] = False
            print(f"Task '{task}' added successfully!")
        else:
            print(f"Task '{task}' already exists.")

    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"Task '{task}' removed successfully!")
        else:
            print(f"Task '{task}' not found.")

    def update_task(self, task, status):
        if task in self.tasks:
            self.tasks[task] = status
            print(f"Task '{task}' updated to {'completed' if status else 'not completed'}.")
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("To-Do List:")
            for task, status in self.tasks.items():
                print(f"- {task} {'(Completed)' if status else '(Not Completed)'}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)

        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)

        elif choice == '3':
            task = input("Enter the task to update: ")
            status = input("Is the task completed? (yes/no): ").strip().lower() == 'yes'
            todo_list.update_task(task, status)

        elif choice == '4':
            todo_list.view_tasks()

        elif choice == '5':
            print("Exiting the To-Do List application.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
