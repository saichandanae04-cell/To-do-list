'''# Create an empty list to store tasks
tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    # Add task
    if choice == '1':
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View tasks
    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks found!")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    # Exit program
    elif choice == '3':
        print("Exiting program. byebye!")
        break

    else:
        print("Invalid choice! Please try again.")'''