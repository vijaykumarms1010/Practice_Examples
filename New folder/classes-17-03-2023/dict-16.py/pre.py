from logic import addTask,present,updateTask,viewTask,removeTask 
# from models import task 

def start():
    exit = False
    while not exit:
        print("0.Exit\n1. Enter Task ID:")
        ch=int(input("Enter ur choice:"))
        if ch ==0:
            exit = True
        if ch==1:
            id = int(input("Enter the Task ID: ")) 
            res = present(id)
            print(res)

            print("0. Go back to menu\n1. Add task information\n2. update task information\n3. view Task information\n4. Remove Task Information")
            hc=int(input("Enter ur Option: "))
            if hc ==1:
                id = int(input("Enter the id: ")) 
                nam=input("Enter the Task name: ")
                des=input("Enter the description: ")
                pri=int(input("Value the priority: "))
                x=task(id,nam,des,pri)
                res = addTask(x) 
                print (res,"\n")
            if hc ==2:
                id = int(input("Enter the id: ")) 
                nam=input("Enter the Task name: ")
                des=input("Enter the description: ")
                pri=int(input("Value the priority: "))
                x=task(id,nam,des,pri)
                res = updaateTask(x) 
                print (res,"\n")
            if hc==3:
                id = int(input("Enter the Task id to view the information: "))
                res = viewTask(id)
                print ( res, "\n")
                # id = int(input("Enter the Task ID:)) 
                # res = present(id) 
                # print(res)
            if ch==4:
                id=int(input('Enter task id to remove:'))
                res=removeTask(id)
                print(res,'\n')




        



    




























# from logic import *

# def main():
#     while True:
#         print("Menu 1")
#         print("1.Enter Task Id")
#         print("0.Exit")
#         ch1=int(input("Enter Your choice:"))

#         if ch1 == 1:
#             taskid=int(input("Enter TaskId:"))
#             print("1.Update Task Info")
#             print('2.View Info')
#             print('3.Remove Info')
#             print('4.Back to menu1')
#             ch2=int(input("Enter Your choice:"))

#             if ch2 == 1:
#                 update_task(taskid)
#             elif ch2 == 2:
#                 view_task(taskid)
#             elif ch2 == 3:
#                 remove_task(taskid)
#             elif ch2 == 0:
#                 continue
#             else:
#                 print("Invalid choice.")
#         elif ch1 == 0:
#             break
#         if ch2 == 0:
#             continue
#         taskname = input("Enter Task Name: ")
#         description = input("Enter Task Description: ")
#         priority = input("Enter Task Priority: ")
#         add_task(taskid, taskname, description, priority)
# main()














































































































































































































































































































# def main():
#     while True:
#         print("\nMenu 1:")
#         print("1. Enter Task ID")
#         print("0. Exit")
#         choice1 = int(input("Enter your choice: "))
        
#         if choice1 == 1:
#             taskid = int(input("Enter Task ID: "))
            
#             print("\nMenu 2:")
#             print("1. Update Task Information")
#             print("2. View Task Information")
#             print("3. Remove Task Information")
#             print("0. Back to Menu 1")
#             choice2 = int(input("Enter your choice: "))
            
#             if choice2 == 1:
#                 update_task(taskid)
#             elif choice2 == 2:
#                 view_task(taskid)
#             elif choice2 == 3:
#                 remove_task(taskid)
#             elif choice2 == 0:
#                 continue
#             else:
#                 print("Invalid choice.")
                
#         elif choice1 == 0:
#             break
        
#         else:
#             print("Invalid choice.")
            
#         if choice2 == 0:
#             continue
            
#         taskname = input("Enter Task Name: ")
#         description = input("Enter Task Description: ")
#         priority = input("Enter Task Priority: ")
#         add_task(taskid, taskname, description, priority)

# # if _name_ == '_main_':
# main()




















































# def TaskId():
#     taskId()
# def exitng():
#     exit()
# def UpdateInfo():
#     updateTask()
# def ViewInfo():
#     view()
# def RemoveInfo():
#     removeTaskInfo()


# def menu1():
#     exit=False
#     while exit == False:
#         print(" 1.Enter Task Id:\n  0.exit ")
#         ch=int(input('Enter choice:'))
#         if ch == 1:
#             Dict1()
#         elif ch==0:
#             end()
#             break
#         def menu2(menu1):
#             while exit == False:
#                print(" 1.Update Task Info:\n  2.View Task Info\n 3.Remove Task Info\n 0.Back to Menu1 ")
#                choice=int(input('Enter choice:'))
#                if choice == 1:
    



        


























































# employees = {}def addWord(name):    if name in employees.keys():        employees[name] = employees[name]+1        return"Name already present, Count added"           else:        employees[name] = 1        return "Name Added"   def viewWord():    return employees.keys()def allWord():    return employeesdef occurWord(inte):    d1=[]    for emp in employees:        if employees[emp]>=inte:            d1.append(emp)    return d1