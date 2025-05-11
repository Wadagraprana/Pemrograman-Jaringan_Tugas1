"""
5025221101
Problem: Simple Arithmetic
Description:
Read two integers A and B from standard input and print their sum,
difference (A-B), product, and integer division (A//B) on separate
lines.
Input:
The input consists of two lines. Each line contains an integer: A on
the first line and B (non-zero) on the second line.
Output:
Print four lines containing the sum, difference, product, and
integer division, each on a new line.
Example Input:
5
2
Example Output:
7
3
10
2
"""

#count
def simple_arithmetic(A, B):
    print(A + B)
    print(A - B)
    print(A * B)
    print(A // B)

#main
if __name__ == "__main__":
    A = int(input())
    B = int(input())
    simple_arithmetic(A, B)
