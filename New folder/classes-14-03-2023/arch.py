# def getSomeWorld():
#     return "HelloWorld!"

# def start():
#     message=getSomeWorld()
#     print(message)
# start()


# def addition(x,y):
#     addition=x+y
#     return addition

# def calladdition():
#     x=float(input("Enter first Number:"))
#     y=float(input("Enter second Number:"))
#     m=addition(x,y)
#     print("The addition of two num:",m)
# calladdition()


# -------------Ex-01-----------

# def addNum(x,y):
#     add=x+y
#     return add
# def callingAdd():
#     x=float(input("Enter first value:"))
#     y=float(input("Enter first value:"))
#     z=addNum(x, y)
#     print("The sum of two numbers is:",z)
# callingAdd()

# -----------------------------------

#--------------- Ex-02 -------------------
# def areaCircle(l,b,h):
#     area=l*b*h
#     return area
# def callArea():
#     l=float(input("Enter length:"))
#     b=float(input("Enter Breadth:"))
#     h=float(input("Enter height:"))
#     x=areaCircle(l, b, h)
#     print('The area of square is:',x)
# callArea()
# Enter length:10
# Enter Breadth:10
# Enter height:10
# The area of square is: 1000.0
#-----------------------------------------------

#------------------Ex-03---------------------

# def area1(m,n,o):
#     z=(m+n+o)/2
#     result=(z*(z-m)*(z-n)*(z-o))**0.5
#     return result
# def callarea1():
#     m=float(input("Enter side n:"))
#     n=float(input("Enter side n:"))
#     o=float(input("Enter side o:"))
#     x=area1(m, n, o)
#     print("The area is:",x)
# callarea1()
# Enter side n:10
# Enter side n:10
# Enter side o:10
# The area is: 43.301270189221

# ------------------------------------


# def fac(x):
#     f=1
#     for i in range(1,int(x)+1):
#         f=f+f*(i)
#         return float(f)
# def start():
#     x=float(input('Enter operand:'))
#     # y=float(input('Enter second operand:'))
#     re=fac(x)
#     print(f'factorial of {x} is {re}')
# start()
# o/p---Enter operand:10
# factorial of 10.0 is 2.0




#--------------------ex-------------------------
# import random

# def rand(x,y):
#     return random.randint(x, y)
# def callrand():
#     x=int(input("Enter first Number:"))
#     y=int(input('Enter last number:'))
#     m=rand(x, y)
#     print(f'The random number b/t {x} and {y} is {m}')
# callrand()
# O/P--Enter first Number:1
# Enter last number:20
# The random number b/t 1 and 20 is 4
#--------------------------------------------------#
