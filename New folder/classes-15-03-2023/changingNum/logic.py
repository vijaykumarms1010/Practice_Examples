import random
def changeNum():

    arr=[]
    for x in range(10):
        arr.append(random.randint(1, 100))
        
    print("1.The random Number list:",arr)

    m=int(input("2.Enter number you want to change:"))
    if m in arr:
        print("The number  is already Present in list.")
        return arr
    else:
        i=int(input(f'3.Enter the index of the number  in the list:'))
        arr.insert(i,m)
        print(f'4.The list after changing the number at index is:',arr)
        return arr
changeNum()

















































# n=int(input("Enter number of elements:"))

    # for i in range(0,n):
    #     ele=int(input())
    #     arr.append(ele)
    # print('The array is:',arr)



#  def callArr():
#     arr=[]
#     n=int(input("Enternumber of elements:"))
#     for i in range(0,n):
#         ele=int(input())
#         arr.append(ele)
#     print("The sum of the elemets of array is:",sum(arr))
#     print('The array is:',arr)
    
# callArr()