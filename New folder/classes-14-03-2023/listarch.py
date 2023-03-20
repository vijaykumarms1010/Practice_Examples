#--------- factorial -------------------------#
#  def get3Multiples(factor):
#     multiples=[factor*1,factor*2,factor*3];
#     return multiples

# def start():
#     factor=5;
#     multiples=get3Multiples(factor)
#     print(multiples)
# start()
# O/p--[5, 10, 15]
#------------------------------------------------#

#--------------- Sum of elemets-----------------------#
# def sum1(a,b):
#     sum=a+b
#     return sum
# def callsum():
#     m=int(input('Enter number:'))
#     n=int(input('Enter number:'))
#     y=sum1(m,n)
#     print('The sum of {} and {} is: {}'.format(m,n,y))
# callsum()
# O/P--Enter number:10
# Enter number:10
# The sum of 10 and 10 is: 20
#---------------------------------------------------#

#----------------------------------------------------#
# def sumArray(arr):
#     return sum(arr)
# def callSum():
#     x=[1,2,3,4,5]
#     y=sumArray(x)
#     print('The sum of the array is:',y)
# callSum()
# O/P---The sum of the array is: 15


# -------------------ex-01-Passing array-------------#
# def arr(x):
#     return sum(arr)

# def callArr():
#     arr=[]
#     n=int(input("Enternumber of elements:"))
#     for i in range(0,n):
#         ele=int(input())
#         arr.append(ele)
#     print("The sum of the elemets of array is:",sum(arr))
#     print('The array is:',arr)
    
# callArr()

# O/P-
# Enternumber of elements:3
# 3
# 3
# 3
# The sum of the elemets of array is: 9
# The array is: [3, 3, 3]
#-------------------------------------------------------#






#---------------------ex-02---Random number-------------#

# import random
# def randomNum(a,b):
#     x=random.randint(a, b)
#     return x
# def callrnd():
#     a=int(input('Enter starting num:'))
#     b=int(input('Enter last number:'))
#     y=randomNum(a,b)
#     print('The random number between {} and {} is {} '.format(a,b,y))
# callrnd()

# O/P---Enter starting num:10
# Enter last number:20
# The random number between 10 and 20 is 13
#-------------------------------------------------------#






#-------------Ex-03-most occured num--------------------------#

# def  mostOccured(list1):
#     return max(set(list1),key=list1.count)


# def callMostoccu():
#     l1=[1,1,2,3,4,4,4,5,6,8,8,8,8,8]
#     x=mostOccured(l1)
#     print("The most occured num in a list is:",x)
# callMostoccu()
# O/P---The most occured num in a list is: 8
#-----------------------------------------------------#








# -----------------Size of string in list------------------#
# def lenOfString(m):
#     result=[]
#     for i in m:
#         result.append(len(i))
#     return result
# def callLenofStr():
#     list1=['how are you','hi','hello world']
#     msg=lenOfString(list1)
#     print(msg)
# callLenofStr()
# o/p--[11, 2, 11]
#------------------------------------------------------------#


#--------------------date datatypes-------------------------#



from datetime import date

def diff_dates(date1, date2):
    return abs(date2-date1).days

def main():
    d1 = date(2013,1,1)
    d2 = date(2023,9,13)
    result1 = diff_dates(d2, d1)
    print ('{} days between {} and {}'.format(result1, d1, d2))
main()




