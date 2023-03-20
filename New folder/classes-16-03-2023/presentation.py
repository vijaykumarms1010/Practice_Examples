from logic import addWord, viewAll, viewwithOccurs, viewWithInput

def init():
    exit = False
    while exit == False:
        print("*** MENU ***")
        print("1. Add a word")
        print("2. view all words.")
        print("3. show all words with number of time it occurs.")
        print("4. view all words with input as how many times it occurs.")
        print("0. Exit")
        ch = int(input("Enter your choice:"))

        if ch == 1:
            word = input("Enter the word:")
            message = addWord(word)
            print(message)
            print()

        elif ch == 2:
            message = viewAll()
            print(message)
            print()

        elif ch == 3:
            i = int(input("Enter the occured num : "))
            message = viewwithOccurs(i)
            if not message:
                print("No such word")
            else:
                print(i, "has occured", message)
        elif ch == 4:
            item = input("Enter the num : ")
            message = viewWithInput(item)
            print(message)
            print()
        elif ch == 0:
            print("--- GoodBye! ---")
            break



























        
# from logic import *


# def init():
#     exit=False
#     while exit == False:
#         print(" 1.Creating Dictionary:\n 2.View Dictionary:\n 3.Add words TO Dictionary\n 4.Occurance of Words\n 0.end ")
#         ch=int(input('Enter choice:'))
#         if ch == 1:
#             Dict1()
#         elif ch == 2:
#             viewDict()
#         elif ch==3:
#             addWords()
#         elif ch==4:
#             Occurance()
#         elif ch==0:
#             end()
#             break

# def Dict1():
#     # # n = int(input("Enter the number of key-value pairs:"))
#     # # for i in range(n):
#     # key = input("Enter the key: ")
#     #     # value = input("Enter the value: ")
#     createDict()

# def viewDict():
#     print("The random Dictionary is:",my_dict)

# def addWords():
#     print("The dictionart:",my_dict)

# def Occurance():
#     print("The number of times word occured:")

# def end():
#     print("Exit from preogram")


        
