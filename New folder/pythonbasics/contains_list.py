def splitwords(string):
    return string.split()

def word_sizes(str_list):
    sizes = []
    for string in str_list:
        words = splitwords(string)
        for word in words:
            sizes.append(len(word))
    return sizes
str_list = ["hello how are you", "How are you", "how are"]
sizes = word_sizes(str_list)
print(sizes)