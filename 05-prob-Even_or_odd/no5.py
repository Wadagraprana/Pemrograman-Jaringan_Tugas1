"""
5025221101
Even or Odd
Description:
Given an integer N, print "Even" if the number is even and "Odd" if
the number is odd.
Input:
A single integer N.
Output:
Print "Even" if N is even, and "Odd" if N is odd.
Example Input:
4
Example Output:
Even
"""

#count
def evenOrOdd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

#main
if __name__ == "__main__":
    n = int(input())
    print(evenOrOdd(n))