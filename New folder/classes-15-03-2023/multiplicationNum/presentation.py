# from logic import previousnum
from logic import multiplicationNum
# def presen():
#     num=int(input('Enter a number:'))
#     prev_num=previousnum(num)
#     print(f'The previous- number of {num} is {prev_num}')


def multiply():
    x=int(input("Enter first num:"))
    y=int(input("Enter second number:"))
    m=multiplicationNum(x, y)
    print(f"The multiplication of {x} and {y} is:",m)
    