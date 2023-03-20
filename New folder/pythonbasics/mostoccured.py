def count_occurrences(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

def find_most_common(arr):
    counts = count_occurrences(arr)
    most_common = None
    max_count = 0
    for num, count in counts.items():
        if count > max_count:
            most_common = num
            max_count = count
    return most_common

list1 = [10,20,301,10,20,30,40,503,30]
common_num = find_most_common(list1)
print(f"The most common number in {list1} is {common_num}.")