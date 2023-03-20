# def get3Multiples(factor):
#     multiples=[factor*1,factor*2,factor*3];
#     return multiples

# def start():
#     factor=3;
#     multiples=get3Multiples(factor)
#     print(multiples)
# start()


def arrayinput():
    arr = input("Enter a list of numbers : ")
    arr = arr.split()
    arr = [int(x) for x in arr]
    return arr

def sumarray(arr):
    total = 0
    for num in arr:
        total += num
    return total

arr = arrayinput()
arraysum = sumarray(arr)
print(f"The sum of the elements in the list is {arraysum}.")