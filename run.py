from colorama import Fore, Style

tasks = []


def addTask():
    new_task = input("Enter the task: ")
    priority = input("Enter the priority: ")
    tasks.append({"Task": new_task, "Priority": priority})
    print(f"Task '{new_task}' Added Successfully")


def listTasks():
    if not tasks:
        print(Fore.RED + "No Tasks" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "List of Tasks" + Style.RESET_ALL)
        sorted_tasks = sorted(tasks, key=lambda task: task['Priority'])
        for index, task in enumerate(sorted_tasks):
            print(Fore.BLUE + f" Task #{index}. {task['Task']}" +
                  f" (Priority: {task['Priority']})" + Style.RESET_ALL)


def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Choose the number you want to delete:"))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task #{taskToDelete} Deleted Successfully")
        else:
            print(f"Task #{taskToDelete} Does Not Exist")
    except ValueError:
        print("Invalid input: Please enter a valid number.")
    except IndexError:
        print(f"Invalid input: Task #{taskToDelete} Does Not Exist.")


if __name__ == "__main__":
    print("Welcome to The To Do-List")

    while True:
        print("\n")
        print("Please select one of the following options:")
        print("------------------------")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            break
        else:
            print("Invalid input, please try again.")

    print("Thank you for using The To Do-list")
