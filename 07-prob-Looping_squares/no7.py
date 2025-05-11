"""
5025221101
Looping Squares
Description:
Given an integer N, print the squares of all numbers from 1 to N,
each on a new line.
Input:
A single integer N.
Output:
Print N lines, each containing the square of integers from 1 to N.
Example input:
3
Example output:
1
4
9
"""

#count
def printSquares(n):
    for i in range(1, n + 1):
        print(i * i)

#main
if __name__ == "__main__":
    n = int(input())
    printSquares(n)
