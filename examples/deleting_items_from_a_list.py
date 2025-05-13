'''
SCOPE is the accessibility and visibility of a variable.
There is GLOBAL scope (which means the entire application can see & access the variable)
There is LOCAL scope (which means the variable can only be seen & accessed from within the code block in which it was created)
'''
tasks = [] # Global variable.

def initializeList():
    # To reference the global variable 'tasks', we must list it as a global here.
    global tasks
    tasks = ["Do homework", "Go to the gym", "Get groceries", "Finish late homework"]
    print(f"INITIAL LIST: {tasks}")
    
# METHOD 1: remove()
print("\nMETHOD 1:")
initializeList() # Populate the list with the initializeList() function.
tasks.remove("Do homework") # Removes the element "Do homework" from the list.
print(f"CURRENT LIST: {tasks}")

# METHOD 2: pop()
print("\nMETHOD 2:")
initializeList() # Populate the list with the initializeList() function.
tasks.pop(0) # Removes the element at index 0 which is "Do homework"
print(f"CURRENT LIST: {tasks}")

# METHOD 3: del
print("\nMETHOD 3:")
initializeList() # Populate the list with the initializeList() function.
del tasks[0] # Removes the element at idnex 0 which is "Do homework"
print(f"CURRENT LIST: {tasks}")

# METHOD 4:
print("\nMETHOD 4:")
initializeList() # Populate the list with the initializeList() function.
# Loop through the list one task at a time.
for task in tasks:
    # Check if the current task contains the word "homework"
    if "homework" in task:
        tasks.remove(task) # If it does, remove that particular task.
print(f"CURRENT LIST: {tasks}")
