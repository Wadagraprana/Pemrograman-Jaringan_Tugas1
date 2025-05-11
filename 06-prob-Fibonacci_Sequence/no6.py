"""
5025221101
Fibonacci Sequence
Problem Statement:
Write a program that reads an integer N and prints the Nth Fibonacci
number. The Fibonacci sequence starts with 0 and 1, and each
subsequent number is the sum of the previous two.
Input Specification:
A single line containing an integer N.
Output Specification:
Print the Nth Fibonacci number.
Example Input:
5
Example Output:
3
"""

#count
def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]

#main
if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
