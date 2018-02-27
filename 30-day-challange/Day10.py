'''
Day 10: Binary Numbers
Task 
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

Input Format

A single integer, n.

Output Format

Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
'''
#!/bin/python

import sys

n = int(raw_input().strip())
totalCount = s = 0
while n >0 :
    if n%2 == 1:
        totalCount += 1
        if totalCount >= s:
            s = totalCount
    else:
        totalCount = 0
    n=n/2
print s
