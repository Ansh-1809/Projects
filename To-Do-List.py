tasks = []
tasks.append("Buy groceries")
tasks.append("Do homework")
print("Your To-Do List:")
for task in tasks:
    print("-", task)
tasks.remove("Buy groceries")
print("\nUpdated To-Do List:")
for task in tasks:
    print("-", task)