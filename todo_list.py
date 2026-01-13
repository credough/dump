tasks = []

while True:
    action = input("Enter add/remove/view/quit").lower()

    if action == "add":
        task = input("Enter task:")
        tasks.append(task)
    elif action == "view":
        print("Tasks:\n", tasks)
    elif action == "remove":
        print("Tasks\n", tasks)
        task = input("Enter task to remove:")
        if task in tasks:
            tasks.remove(task)
    elif action == "quit":
        break
    else:
        print("Invalid action")

        