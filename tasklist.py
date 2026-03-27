def manage_tasks():
    tasks = []
    while True:
        print("\n--- Task Manager ---")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("0. Return to main menu")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            new_task = input("Enter task description: ")
            tasks.append(new_task)
        elif choice == '2':
            if not tasks:
                print("Task list is empty.")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
        elif choice == '3':
            try:
                num = int(input("Enter task number to remove: "))
                tasks.pop(num - 1)
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif choice == '0':
            break
