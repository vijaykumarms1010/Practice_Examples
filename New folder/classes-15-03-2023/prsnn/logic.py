import random
l1=[]

def creatList():
    l1.clear()
    for i in range(0,10):
        l1.append(random.randint(0,100))
    return l1

def viewList():
    return l1

def change(a,b):
    if a not in l1:
        return "The num not in the list"
    elif b in l1:
        return "The num already in list"
    else:
        i = l1.index(a)
        l1[i] = b
        return "number has changed"

def delete(ele):
    if ele in l1:
        l1.remove(ele)
        return "Number removed"
    else:
        return "num not found"
        
def asc():
        asc=l1.copy()
        asc.sort()
        return asc
        
def dec():
    dec=l1.copy()
    dec.sort(reverse=True)
    return dec




























































import random
randomlist = []
def randomList(): 
    for i in range(0,10):
        n = random.randint(0,100)         
        randomlist.append(n)
def view():
    return randomlist
def change(a,b): 
    if a not in randomlist:
        return "Num not in list"
    elif b in randomlist:
        return "Num already in list"
    else:
        i = randomlist.index(a) 
        randomlist[i] = b
        return "Num changed"
def removeelem(ele):
    if ele in randomlist:
        randomlist.remove(ele)
        return "Num removed"
    else:
        return "No such num"
def asc():
    asc = randomlist.copy()
    asc.sort()
    return asc
def des():
    des = randomlist.copy()
    des.sort(reverse=True)
    return des
        
        































#         import random
# def menu():
#     print("Menu:")
#     print("1.Generate list:")
#     print("2.View list:")
#     print("3.Change the number in List:")
#     print("3.1. Enter number you want to change:")
#     print("3.2. Enter number which should replace:")
#     print("3.3. check whether Number already present:")
#     print("4. Remove Number from list:")
#     print("0. Exit")

#     choice=input("Enter your choice:")
#     if choice== '1':
#          arr=[]
#          for x in range(10):
#              arr.append(random.randint(1, 100))
#          print("The random Number list:",arr)
#          pass
#     elif choice == '2':
#         print("The list of Numbers is:",arr)
#     elif choice == '3':
#         print("Change the number in the list.")
#         pass
#     elif choice=='3.1':
#          x=print("Enter number you want to change:")
#          if x in arr:
#             print("The Number is already present.")
#          else:
#             print("Number not in list.")
#     elif choice== '3.2':
#         print("Enter Number you want to Replace:")
#     elif choice == '3.3':
#         if number in arr:
#             print("Number  ")
# menu()