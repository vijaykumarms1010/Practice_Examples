
from logic import randlist,randomList, view, change, removeelem, asc,des,occur
import operator as op
def fillList():
    randomList()
    print("Filled 10 random nos")
    print()
def viewList():
    message = view()
    # print(message)
    print('The random list is:',randlist)
def changeNum():
    a = int(input("Enter the no:"))
    b = int(input("Enter the new no:"))
    message = change(a,b)
    print(message)
    print()
def remove():
    ele = int(input("Enter the num to remove:"))
    message = removeelem(ele)
    print(message)
    print()
    
def sortasc():
    message = asc()
    print(message)
def sortdes():
    message = des()
    print(message)
def counting():
    res =occur()
    print(res) 
    
    
def init():
    exit = False
    while exit == False:
        print("1.Fill up list with 10 random nos")
        print("2.View all the list")
        print("3.Change the no")
        print("4.Remove element")
        print("5.Sort in ascending")
        print("6.Sort in descending")
        print("7.Occurance of num")
        print("0.exit")
        ch = int(input("Enter choice:"))
        if ch == 1:
            fillList()
        elif ch == 2:
            viewList()
        elif ch == 3:
            changeNum()
        elif ch == 4:
            remove()   
        elif ch == 5:
            sortasc()
        elif ch == 6:
            sortdes()
        elif ch==7:
             counting()
        elif ch == 0:
            break




























# from logic import randomList,viewList,removeele,asc,des #occuraceNum#
# def init():
#     exit = False
#     while not exit:
#         print("1.Fill up list with 10 random nos")
#         print("2.View all the list")
#         print("3.Change the no")
#         print("4.Remove element")
#         print("5.Sort in ascending")
#         print("6.Sort in descending")
#         # print('7. Occurance of num:')
# # get all numbers and its occurences.
# # you have to print in the random list, each number how many times it occurs
#         print("0.exit")
#         ch = int(input("Enter choice:"))
#         print()
#         if ch==0:
#             exit=True
#         if ch == 1:
#             def viewList():
#                 viewList()
#                 print("Filled 10 random num:")
              
#         elif ch == 2:
#             def viewList():
#                 message = view()
#                 print(message)
               
#         elif ch == 3:
#             def changeNum():
#                 a = int(input("Enter the no:"))
#                 b = int(input("Enter the new no:"))
#                 message = change(a, b)
#                 print(message)
#                 print()
#         elif ch == 4:
#             def remove():
#                 ele = int(input("Enter the num to remove:"))
#                 message = removeelem(ele)
#                 print(message)
#                 print()
#         elif ch == 5:
#             def sortasc():
#                 message = asc()
#                 print(message)
#         elif ch == 6:
#             def sortdes():
#                 message = des()
#                 print(message)
#         # elif ch == 7:
#         #     def occurace():
#         #         n=occuraceNum()
#         #         g=print=("Enter value you want to search:")
#         #         print("The most occured num:",g)
                
#         elif ch == 0:
#             print("---Good Bye----")
#             break


















