"""
5025221101
Double the Number
Description:
Write a program that reads a single floating-point number from the
input and prints that number multiplied by 2 to the output. Your
program's output is considered correct if it is within a 0.01 margin
of error from the expected result.
Input:
A single line containing a floating-point number n (0 < n < 10000).
Output:
Output the number n multiplied by 2. Your output is considered
correct if it is within 0.01 of the product's actual value.
Sample Input:
2.5
Sample Output:
5.0
"""

#count
def doubleNumber(n):
    return n * 2

#main
if __name__ == "__main__":
    n = float(input())
    print(f"{doubleNumber(n):.1f}")