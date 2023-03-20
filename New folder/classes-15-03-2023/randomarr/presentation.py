# from logic import addNumbers
# def Addition():
#     x=int(input("Enter First num:"))
#     y=int(input("Enter second Number:"))
#     sum=addNumbers(x,y)
#     print(f"The sum of {x} and {y} is {sum} ") 

# from logic import substction
# def init():
#     x=int(input("Enter first number:"))
#     y=int(input("Enter second number:"))
#     subt=substction(x, y)
#     print(f'The substaction of {x} and {y} is {subt}')
    

# from logic import multiplication
# def init():
#     x=int(input("Enter first number:"))
#     y=int(input("Enter seond number:"))
#     m=multiplication(x, y)
#     print(f"The multiplication of {x} and {y} is {m}")


from presentation import randomArr
def views():
    exit = False
    while exit == False:
        print("1.List with random numbers: ")
        print("2.view List:")
        print("3.Change Number:")
        print("4. Remove element:")
        print("5.Sort in Ascending order:")
        print("6. Sort in descending:")
    ch=int(input("Enter choice:"))
    if ch==1:
        def viewList() :
            print(arr)