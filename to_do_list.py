tasks = []

# Function to display options.
def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
    
# Function to add a task.
def add_task():
    new_task = input("Enter a task: ") # Prompt the user to enter a new task.
    tasks.append(new_task) # Add the task to the list.
    print(f"Task {new_task} has been added successfully.") # Confirm that it has been added successfully.
    print(tasks) # Print out the tasks list.
    
# Function to view all tasks in the list.
def view_tasks():
    print("This needs to be implemented still.") # Complete this please.

# Function to delete a task in the list.
def delete_task():
    print("This method needs to be implemented still.") # Complete this please.
    
# Main function (start of the program)
def main():
    # Infinite loop
    while True:
        display_menu()
        choice = input("What would you like to do? ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
            
main()