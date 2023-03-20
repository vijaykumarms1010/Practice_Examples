# from presentation import 

dict = {}

def addWord(word):
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1
        return "Word has been added"

def viewAll():
        return dict
    
def viewwithOccurs():
    return dict.items()

def viewWithInput(i):
     emt = []
     for n in i:
        if dict(n) in i:
         return emt.append(i)
     else:
         return "Word not found"













# my_dict = {}

# def createDict():
#     return my_dict
#     # my_dict[key] = value
#     # print()

# def view():
#     print(my_dict)


# def addWords():
#     return my_dict
    
# def WordOccurnc():
#     return my_dict
    
# def ending():
#     print()
















#     word = input("Enter a word: ")
#     value = int(input("Enter a value: "))
# # add word and value to the dictionary
#     my_dict[word] = value
#     print(my_dict)


 






























































# def rev_list(l1,size):
#     if(size == 1):
#         return l1
#     elif (size == 2):
#         l1[0],l1[1]=l1[1],l1[0]
#         return l1
#     else:
#         i=0
#         while(i<size//2):
#             l1[i],l1[size-1]=l1[size-1],l1[i]
#             if((i!=i+1 and size-i-1!=size-i-2) and (i!=size-i-2 and size-i-1!=i+1)):
#                 l1[i + 1], l1[size - i - 2] = l1[size - i - 2], l1[i + 1]
#             i += 2
#         return l1


