"""
5025221101
Counting Characters
Problem Statement:
Write a program that reads a string and prints a count of each
character in the string.
Input Specification:
A single line containing a string.
Output Specification:
Print each character and its count in the format character=count. Each
character should appear only once in the output, in the order they
appear in the input string.
Example Input:
hello
Example Output:
h=1
e=1
l=2
o=1
"""

#count
def countCharacters(s):
    charCount = {}
    
    for char in s:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1

    for char in s:
        if char in charCount:
            print(f"{char}={charCount[char]}")
            del charCount[char]

#main
if __name__ == "__main__":
    s = input()
    countCharacters(s)