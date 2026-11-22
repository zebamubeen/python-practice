tasks = []

while True:
    print("\n1. Add task  2. View tasks  3. Remove task  4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        tasks.append(input("Task: "))
    elif choice == "2":
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")
    elif choice == "3":
        number = int(input("Task number to remove: "))
        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please pick 1-4.")