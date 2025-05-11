"""
5025221101
Positive Sum
Description:
Given a sequence of integers, print the sum of the positive integers
only.
Input:
The first line contains a single integer N, the number of integers
in the sequence.
The following N lines each contain a single integer.
Output:
Print a single integer – the sum of the positive integers in the
given sequence.
Example Input:
5
1
-2
3
-4
5
Example Output:
9
"""

#count
def positive_sum(n, numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

#main
if __name__ == "__main__":
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    print(positive_sum(n, numbers))
