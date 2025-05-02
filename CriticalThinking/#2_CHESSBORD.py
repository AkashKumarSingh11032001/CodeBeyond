'''
--- Algorithm: Chessboard
--- Description: This program to tell the chess square color is black or white. Based on the chessboard pattern, it uses the formula (x + y) % 2 == 0 for white and (x + y) % 2 == 1 for black.
--- Input: Two integers x and y representing the coordinates of the square on the chessboard.
--- Output: The color of the square at the given coordinates (black or white).
'''

def chessboard(x, y):
    if (x + y) % 2 == 0:
        return "black"
    else:
        return "white"
    
if __name__ == "__main__":
    x, y = input("Enter the coordinates (x y): ").split()
    dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    color = chessboard(dict[x], int(y))
    print(f"The color of the square at ({x}, {y}) is {color}.")