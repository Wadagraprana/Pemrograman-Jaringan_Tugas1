"""
5025221101
Palindrome Checker
Problem Statement:
Write a program that reads a string and prints "Palindrome" if the
string is a palindrome (reads the same forwards and backwards) and
"Not Palindrome" otherwise. Consider only alphanumeric characters and
ignore case.
Input Specification:
A single line containing a string.
Output Specification:
Print "Palindrome" if the string is a palindrome, otherwise print "Not
Palindrome".
"""

#ubah ke lower
def clean_string(s):
    cleaned = ""
    for c in s:
        if c.isalnum():
            cleaned += c.lower()
    return cleaned

#check palindrome
def is_palindrome(s, i, j):
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return is_palindrome(s, i + 1, j - 1)
#main
if __name__ == "__main__":
    s = input()
    cleaned = clean_string(s)
    print("Palindrome" if is_palindrome(cleaned, 0, len(cleaned) - 1) else "Not Palindrome")
