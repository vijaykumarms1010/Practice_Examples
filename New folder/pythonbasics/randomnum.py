import random

def random_num():
    return random.randint(10, 20)

def list1():
    return [random_num() for _ in range(10)]

list2 = list1()
print(f" List of random numbers: {list2}")