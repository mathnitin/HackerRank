'''
Day 3: Intro to Conditional Statements

Task 
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not n is weird.

Input Format

A single line containing a positive integer, n.

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.
'''
#!/bin/python

import sys


n = int(raw_input().strip())
if n%2 != 0:
    print 'Weird'
else:
    if n >= 2 and n <= 5:
        print 'Not Weird'
    elif n >= 6 and n <= 20:
        print 'Weird'
    else:
        print 'Not Weird'