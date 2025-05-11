"""
5025221101
Shift-Matrix-Element
Description:
You are given a 3x3 matrix, and you need to shift its elements to the right by a specified number of positions.
Input:
• The first three lines contain the 3x3 matrix with integer values.
• The fourth line contains a single integer, n, indicating how many positions the elements of the matrix should be shifted to the right.
Output:
Output the matrix after it has been shifted to the right by n positions.
Example Input:
1 2 3
4 5 6
7 8 9
1
Example Output:
4 1 2
7 5 3
8 9 6
"""

#shift clockwise
def rotateMatrix(mat):
    if not len(mat):
        return

    top, bottom = 0, len(mat) - 1
    left, right = 0, len(mat[0]) - 1

    while left < right and top < bottom:
        prev = mat[top + 1][left]

        for i in range(left, right + 1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr
        top += 1

        for i in range(top, bottom + 1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr
        right -= 1

        for i in range(right, left - 1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr
        left += 1

#rotate
def shiftMatrix(mat, n):
    for _ in range(n % 9):
        rotateMatrix(mat)

#main
if __name__ == "__main__":
    matrix = [list(map(int, input().split())) for _ in range(3)]
    
    n = int(input())

    shiftMatrix(matrix, n)

    for row in matrix:
        print(*row)
