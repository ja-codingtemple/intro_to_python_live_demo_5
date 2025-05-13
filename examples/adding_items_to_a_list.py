# Create the original list.
tasks = ["Do homework", "Go to the gym", "Get groceries"]
# Print out the original list.
print(tasks)


# Prompt the user to add an item to the list, save their response in a variable called 'new_task'
new_task = input("What do you want to add to the list? ")
tasks.append(new_task) # Add new_task to the list.
print(tasks) # Print out the list.

# Append "Walk the dog" to the list.
tasks.append("Walk the dog")
# Print out the list.
print(tasks)