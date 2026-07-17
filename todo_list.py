tasks = []
while True:
    print("""

    ====== TO-DO LIST ======

    1. View Tasks
    2. Add Task
    3. Remove Task
    4. Exit""")
    choose_option = int(input("Choose an option: "))

    if choose_option == 1 and len(tasks) == 0:
        print("\nNo tasks available.")
        print("Press 2 if you want to enter a task.")
    elif choose_option == 1 and len(tasks) != 0:
        print(tasks)

    elif choose_option == 2:
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print("Task added successfully.")

    elif choose_option == 3 and len(tasks) != 0:
        try:
            remove_task = input("Enter the task that you want to remove: ")
            tasks.remove(remove_task)
            print("Task removed successfully!")
        except ValueError:
            print("Task not present")
    elif choose_option == 3 and len(tasks) == 0:
        print("No task to remove.")

    elif choose_option == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid input!")