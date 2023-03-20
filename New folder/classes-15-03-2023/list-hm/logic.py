import random
from collections import Counter
randlist = []
def randomList():
    randlist.clear()
    for i in range(0,10):
        n = random.randint(0,100)
        randlist.append(n)
def view():
    return randlist
def change(a,b):
    if a not in randldist:
        return "Num not in list"
    elif b in randlist:
        return "Num already in list"
    else:
        i = randlist.index(a)
        randlist[i] = b
        return "Num changed"
def removeelem(ele):
    if ele in randlist:
        randlist.remove(ele)
        return "Num removed"
    else:
            return "No such num"
def asc():
    asc = randlist.copy()
    asc.sort()
    return asc
def des():
    des = randlist.copy()
    des.sort(reverse=True)
    return des
def occur():
    a=[]
    b=[]
    count=0
    for i in randlist:
        c=randlist.count(i)
        count=c
        a.append(i)
        b.append(count)
        d=dict(zip(a,b))
        return d









    # counts={}
    # for e in randlist:
    #     counts[e]=randlist.count(e)
    #     return 
    # # k=[]
    # for i in k:
    #     if k[randlist]>=count:
    #         k.append(randlist)
    # return 





































# import random
# # from collections import Counter
# l1=[]
# def randomList():
#     l1.clear()
#     for x in range(1,10):
#         l1.append(random.randint(1, 100))
#     return l1
# def viewList():
#     returnl1
# def changeNum(a,b):
#     if a not in l1:
#         return "Number not  exists"
#     elif b in l1:
#         return "Number already present in list"
#     else:
#         i=al1index(a)
#         l1[i]=b
#         return "Number Changed"
# def removeele(ele):
#     if ele in l1:
#         l1.remove(ele)
#         return "Number Removed"
#     else:
#         return "Number Not Present"
# def asc():
#     asc=l1.copy()
#     asc.sort()
#     return asc
# # def occuraceNum(arr,x):
# #     Count=0
# #     for ele in arr:
# #         if (ele == x):
# #             count =count+1
# #     return count
# def des():
#     des = l1.copy()
#     des.sort(reverse=True)
#     return des