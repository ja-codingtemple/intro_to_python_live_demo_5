'''
Each item in a list (otherwise known as an array) is called an element.
Each element in a list has an index number, which is a number that represents its position in the list.
Index numbers begin at 0. So the first element in a list has an index of 0.
'''
#             0               1                2
tasks = ["Do homework", "Go to the gym", "Get groceries", "Walk the dog", "Go to church"]

'''
To retrieve elements by their index number, you must reference the list itself, followed by [], and specify the index in []
'''
print(tasks[0]) # This retrieves "Do homework" by its index of 0
print(tasks[1]) # This retrieves "Go to the gym" by its index of 1
print(tasks[2]) # This retrieves "Get groceries" by its index of 2
print(len(tasks)) # This prints out the length of the list 'tasks'

# LOOPING THROUGH LISTS: Method 1
print("\nMETHOD 1:")
for task in tasks:
    print(task)
    
# LOOPING THROUGH LISTS: Method 2
print("\nMETHOD 2:")
for index in range(len(tasks)):
    print(tasks[index])
    
# LOOPING THROUGH LISTS: Method 3
print("\nMETHOD 3:")
for index in range(len(tasks)):
   print(f"{index + 1}. {tasks[index]}")
   
# LOOPING THROUGH A LIST: Method 4:
print("\nMETHOD 4:")
for number, task in enumerate(tasks, 1):
    print(f"{number}. {task}")