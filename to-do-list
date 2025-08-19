def todo_list():
    tasks = []

    while True:
        print("\n📋 To-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            print("✅ Task added!")

        elif choice == "2":
            print("\nYour Tasks:")
            if not tasks:
                print("No tasks yet.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "3":
            task_no = int(input("Enter task number to remove: "))
            if 0 < task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"🗑️ Removed: {removed}")
            else:
                print("Invalid task number.")

        elif choice == "4":
            print("👋 Exiting To-Do List.")
            break
        else:
            print("Invalid choice, try again.")

todo_list()
