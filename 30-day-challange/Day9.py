'''
Day 9: Recursion
Task 
Write a factorial function that takes a positive integer, N as a parameter and prints the result of N!(N factorial).

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.

Input Format

A single integer, N (the argument to pass to factorial).

Output Format

Print a single integer denoting N!.

Sample Input

3
Sample Output

6
'''
#!/bin/python

import sys

def factorial(n):
    # Complete this function
    if n > 1:
        return n*factorial(n-1)
    elif n == 1:
        return 1

if __name__ == "__main__":
    n = int(raw_input().strip())
    result = factorial(n)
    print result
