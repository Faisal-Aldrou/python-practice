to_do = []
while True:
    task = input("enter a task (or 'done' to stop):")
    if task == 'done':
        break
    else:
        to_do.append(task)

print("your tasks are: ")
for task in to_do:
    print(task)

