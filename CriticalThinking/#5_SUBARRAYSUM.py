def subarray_sum(s, n):
    prefix_sum = 0
    prefix_map = {0: -1}  # Initialize with 0 to handle subarrays starting from index 1
    count = 0
    last_index = -1  # Tracks the end of the last valid subarray

    for i, num in enumerate(A):
        prefix_sum += num

        # If the prefix_sum exists in the map, check for non-overlapping condition
        if prefix_sum in prefix_map and prefix_map[prefix_sum] >= last_index:
            count += 1
            last_index = i  # Update the last valid subarray's end index

        # Update the prefix_map with the current prefix_sum
        prefix_map[prefix_sum] = i

    return count



n = int(input())
s = list(map(int, input().split()))

print(subarray_sum(s, n))

