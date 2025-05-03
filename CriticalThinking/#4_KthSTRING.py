def kthString(strings, k):
    # Dictionary to store the frequency of each string
    frequency_map = {}
    # List to store unique strings in the order they appear
    unique_strings = []

    for string in strings:
        if string not in frequency_map:
            frequency_map[string] = 1
        else:
            frequency_map[string] += 1
    
    # Only add the string to unique_strings if it's the first time we see it
    for string in strings:
        if frequency_map[string] == 1:
            unique_strings.append(string)

    # Check if k is valid and there are enough unique strings
    if k <= 0 or len(unique_strings) < k:
        return -1
    else:
        return unique_strings[k - 1]

'''
def kthString(strings, k):
    # Dictionary to store the frequency of each string
    frequency_map = {}

    for string in strings:
        if string not in frequency_map:
            frequency_map[string] = 1
        else:
            frequency_map[string] += 1

    # Iterate over the input strings to find the kth unique string
    unique_count = 0
    for string in strings:
        if frequency_map[string] == 1:
            unique_count += 1
            if unique_count == k:
                return string

    # If there are fewer than k unique strings
    return -1
'''

n = int(input())
s = [input() for _ in range(n)]
k = int(input())

print(kthString(s, k))


