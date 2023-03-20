
##########################################################


# def countWords(x):
#     count=x.split()
#     return len(count)
# def callcount():
#     x=input("Enter string:")
#     res=countWords(x)
#     print("The number of words in string:",res)
# callcount()

# O/P---Enter string:  python language lectures
# The number of words in string: 3


def count(m,n):
    result=m.count(n)
    return result
def callCount():
    m=input("Enter String:")
    n=input("Enter letter to search in string:")
    count=m.count(n)
    if count == 0:
        print('-1')
    else:
        print("The number of times {} appears in {} is:{}".format(n,m,count))
callCount()
# O/P--Enter String:viijay
# Enter letter to search in string:m
#                                 -1

# Enter String:viijay
# Enter letter to search in string:i
# The number of times i appears in viijay is:2