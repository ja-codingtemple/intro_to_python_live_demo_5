#            Index 0        Index 1           Index 2
tasks = ["Do homework", "Go to the gym", "Get groceries"]

for task_number, task in enumerate(tasks, 1):
    print(f"{task_number}. {task}")
    
# Prompt the user for which task they waant to delete. Cast the type to integer. Remember: input() returns a string by default.
choice = int(input("Which task do you want to delete? ")) 
'''
Decrease the value of choice by 1 because we are removing an item by its index.
The item number displayed to the user is not the same as the index number. It is 1 higher.
So, we have to reduce that vaue by 1 to get the true index for the item they want to remove.
'''
choice = choice - 1 # Decrease the value of choice by 1.
tasks.pop(choice) # Remove the element at the index specified.

# ALTERNATIVE APPROACH: This deos the same thing as pop()
# del tasks[choice]

print(tasks)