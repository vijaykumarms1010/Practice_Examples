from logic import *
def dictprgm():
    exit = False
    while(exit==False):
        print("\nMenu1:")
        print("1.Enter choice:")
        print('0.Exit')
        ch1=int(input("Enter your choice:"))
        if ch1 == 1:
            taskId=int(input("Enter TaskId:"))
            print("\n Menu2")
            print('1. Update Task Info')
            print("2. View Task Info")
            print("3. Remove Task Info")
            print("0. Back to Menu1")
            ch2=int(input("Enter Tour choice:"))
            if ch2 == 1:
                taskName= input("Enter taskName:")
                Desc=input("Enter Task Description:")
                Priority=input("Enter Task Priority:")
                update_task(taskId,taskName,Desc,Priority)
            elif ch2 == 2:
                task=view_task(taskId)
                if taskId != "Task ID not Found.":
                    print("Task ID: ",task[0])
                    print("Task Name: ",task[1])
                    print("Task Description: ",task[2])
                    print("Task priority:",task[3])
                else:
                    print(task)
            elif ch2==3:
                remove_task(taskId)
            elif ch2==0:
                continue
            else:
                print("Invalid Choice.")
        elif ch1==0:
            break
        else:
            print("Invalid choice.")
        if ch2==0:
            continue
        taskName=input("Enter task Name:")
        Desc=input("Enater task Description:")
        Priority=input("Enter task priority:")
        add_task(taskId,taskName,Desc,Priority)
dictprgm()
