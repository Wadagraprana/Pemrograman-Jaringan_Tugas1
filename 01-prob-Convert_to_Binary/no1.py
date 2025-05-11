"""
5025221101
Convert to Binary
Problem Statement:
Write a program that reads a non-negative integer N and prints its
binary representation.
Input Specification:
A single line containing a non-negative integer N.
Output Specification:
Print the binary representation of N.
Example Input:
5
Example Output:
101
"""

#convert
def convert_to_binary(n):
    binary = ""
    if n == 0:
        return "0"
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

#main
if __name__ == "__main__":
    n = int(input())
    print(convert_to_binary(n))
