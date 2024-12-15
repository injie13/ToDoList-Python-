# To do List
  # 1. Add a task
  #2. Delete a task
  # 3. List the tasks
  # 4. Quit
def addTask():
  task = input("Enter the task you want to add: ")
  tasks.append(task)
  print(f"Task '{task}' has been added to the list")
def deleteTask():
  listTasks()
  try:
    taskToDelete = int(input("Enter the number you want to delete: "))
    if taskToDelete >= 0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} has been removed.")
    else:
      print(f"Task #{taskToDelete} was not found.")
  except:
    print("Invalid Input. Try again.")
  
def listTasks():
  if not tasks:
    print("There are no tasks yet.")
  else:
    print("Here are your tasks: ")
    for index, task in enumerate(tasks):
      print(f"Task #{index + 1}. {task}.")

  


tasks = []

if __name__ == "__main__":
  
  print("Welcome to the ToDOList App. ")
  print("\n")
  while True:
    print("Please select one of the following options")
    print("__________________________________________")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. List the tasks")
    print("4. Quit")
  
    choice = input("Enter a choice: ")
  
    if (choice == "1"):
      addTask()
    elif (choice == "2"):
      deleteTask()
    elif (choice == "3"):
      listTasks()
    elif (choice == "4"):
      break
    else:
      print("Invalid number. Try again")
  
  print("GoodBye!!!")
  