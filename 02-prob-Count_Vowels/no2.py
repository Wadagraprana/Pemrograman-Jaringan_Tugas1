"""
5025221101
Count Vowels
Problem Statement:
Write a program that reads a string and prints the number of vowels
(a, e, i, o, u) in the string. Consider both lowercase and uppercase
vowels.
Input Specification:
A single line containing a string.
Output Specification:
Print the number of vowels in the string.
Example Input:
Hello World
Example Output:
3
"""

#count
def countVowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

#main
if __name__ == "__main__":
    s = input()
    print(countVowels(s))
