'''
Day 5: Loops
Task 
Given an integer, n, print its first 10 multiples. Each multiple n*i (where 1 <= i <= 10) should be printed on a new line in the form: n x i = result.

Input Format

A single integer, n.

Output Format

Print 10 lines of output; each line i (where 1 <= i <= 10) contains the result of n*i in the form: 
    n x i = result.
'''
#!/bin/python

import sys


n = int(raw_input().strip())
i = 1
#for i in range(1,11):
while i <= 10:
    print str(n), "x", str(i), "=", str(n*i)
    i += 1
