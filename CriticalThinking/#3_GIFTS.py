def find_youngest_member(n, m, gifts):
    tempDect = {}
    
    # If no gifts were exchanged, return n (all members are eligible)
    if len(gifts) <= 0:
        return n

    # Count the number of gifts received by each member
    for i in range(m):
        if gifts[i][1] in tempDect:
            tempDect[gifts[i][1]] += 1
        else:
            tempDect[gifts[i][1]] = 1

    # Check if any member received gifts from all others
    for k, v in tempDect.items():
        if v == m:
            return k

    # If no such member is found, return -1
    return -1

# Input reading
if __name__ == "__main__":
    # Read number of family members and number of gifts
    n, m = map(int, input().split())
    
    # Read gift data
    gifts = [tuple(map(int, input().split())) for _ in range(m)]
    
    # Find and print the youngest member
    print(find_youngest_member(n, m, gifts))