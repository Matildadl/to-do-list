from colorama import Fore, Style

tasks = []

def addTask():
    new_task = input("Enter the task: ")
    priority = input("Enter the priority: ")
    tasks.append({"task": new_task, "priority": priority})
    print(f"Task '{new_task}' added successfully")

def listTasks():
    if not tasks:
        print(Fore.RED +"No tasks" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "List of tasks" + Style.RESET_ALL)
        sorted_tasks = sorted(tasks, key=lambda task: task['priority'])
        for index, task in enumerate(sorted_tasks):
            print(Fore.BLUE + f" task #{index}. {task['task']} (priority: {task['priority']})" + Style.RESET_ALL)

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("choose the number you want to delete:"))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"task #{taskToDelete} deleted successfully")
            
        else:
            print(f"task #{taskToDelete} does not exist")
    except:
        print("invalid input")

if __name__ == "__main__":
    print("Welcome to the to do-list")
    while True:
        print("\n")
        print("please select one of the following options")
        print("------------------------")
        print("1. Add a task")
        print("2. delete a task")
        print("3. list tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        elif(choice == "4"):
            break
           
        else:
            print("Invalid input, please try again.") 

    print("Thank you for using the to do-list")