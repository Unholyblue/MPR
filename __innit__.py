import pyinputplus as pip

def main():
    tasks = []
    Status_No = "Not Done"
    Status_Yes = "Done"
    while True:
        print("\n====== To-Do List ======")
        print("1. Add a Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            NumTasks  = pip.inputNum("How many tasks you want to add: ")
            for i in range(NumTasks):
              TaskInput = input("Input the Task: ")
              tasks.append(TaskInput)

        if choice == "2":
            print("\n===== Tasks =====")
            for n,task in enumerate(tasks):
                print("{}. {} - {}".format(n+1, task, Status_No))

        if choice == "3":
           TaskChoice = input("Enter the task you want to mark as Done: ")
           print("\n===== Tasks =====")
           for n,task  in enumerate(tasks):
               if n+1 == int(TaskChoice):
                  print("{}. {} - {}".format(n+1, task, Status_Yes))
               else:
                   print("{}. {} - {}".format(n+1, task, Status_No))
        if choice == "4":
            break
main()