#-------------------ex ------------------------
# def countWords(x):
#     res=len(x.split())
#     return res
# def start():
#     x=input("Enter string:")
#     y=countWords(x)
#     print("The Number of words in String:",y)
# start()
# ---------------------------------------------
# O/P--Enter string:count numbers in string
# The Number of words in String: 4
#------------------------------------------------



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
#########################################

# ------------------------Ex-------------------------
# def countWords(x):
#     y=len(x.split())
#     return y
# def callfun():
#     x=input("Enter string:")
#     m=countWords(x)
#     print("The number of words in string:",m)
# callfun()
# -------------------------------------
# O/P---Enter string:vij vij vhi
# The number of words in string: 3
# ----------------------------------------------------



def countWords(x):
    count=x.split()
    return len(count)
def callcount():
    x=input("Enter string:")
    res=countWords(x)
    print("The number of words in string:",res)
callcount()

# O/P---Enter string:  python language lectures
# The number of words in string: 3
