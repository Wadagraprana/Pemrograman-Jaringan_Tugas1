"""
5025221101
Problem Statement: Sum of First N Integers
Description:
Write a program that reads a single integer N from standard input
and calculates the sum of the first N integers, where N can be any
integer (positive, negative, or zero). The sequence of the first N
integers starts from 1 and goes up to N if N is positive, or starts
from -1 and goes down to N if N is negative. If N is 0, the sum is
considered 0.
Input:
The input consists of a single line containing a single integer N
(-1000 ≤ N ≤ 1000).
Output:
The output should be a single line containing a single integer, the
sum of the first N integers.
Example Input 1:
5
Example Output 1:
15
Explanation 1:
The sum of the first 5 integers (1 + 2 + 3 + 4 + 5) is 15.
Example Input 2:
-3
Example Output 2:
-6
Explanation 2:
The sum of the first -3 integers (-1 + -2 + -3) is -6.
"""

def sum_first_n(n):
    if n > 0:
        return sum(range(1, n + 1))
    elif n < 0:
        return sum(range(-1, n - 1, -1))
    else:
        return 0

if __name__ == "__main__":
    n = int(input())
    print(sum_first_n(n))