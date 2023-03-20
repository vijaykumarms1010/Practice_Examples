def substract(x,y): # logic part
    result=x-y
    return result

def startApp(): #presentation
    x=float(input("Enter first operand:"))
    y=float(input("Enter second operand:"))
    z=substract(x, y)
    print("The Result is:",z)
startApp()
# Enter first operand:10
# Enter second operand:2
# The Result is: 8.0