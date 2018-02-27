'''
Day 6: Let's Review
Task 
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Input Format

The first line contains an integer, T (the number of test cases). 
Each line i of the T subsequent lines contain a String, S.

Output Format

For each String Sj (where 0<j<T-1), print Sj's even-indexed characters, followed by a space, followed by Sj's odd-indexed characters.

Sample Input

2
Hacker
Rank
Sample Output

Hce akr
Rn ak
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python

import sys

noOfInput = int(raw_input())
for i in range(0, noOfInput):
    inputString = str(raw_input().strip())
    evenString = ""
    oddString = ""
    for i in range(0, len(inputString)):
        if i%2 == 0:
            evenString += str(inputString[i])
        else:
            oddString += str(inputString[i])
#    for i in range(0, len(inputString),2):
#        evenString = evenString+str(inputString[i])
#    for i in range(1, len(inputString),2):
#        oddString = oddString+str(inputString[i])
    print evenString, oddString
