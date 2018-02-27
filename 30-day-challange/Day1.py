'''
Day 1:- Data Types
Input Format

The first line contains an integer that you must sum with . 
The second line contains a double that you must sum with . 
The third line contains a string that you must concatenate with .

Output Format

Print the sum of both integers on the first line, the sum of both doubles (scaled to  decimal place) on the second line, and then the two concatenated strings on the third line.

Sample Input

12
4.0
is the best place to learn and practice coding!
Sample Output

16
8.0
HackerRank is the best place to learn and practice coding!
'''
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
myInt = None
myFloat = None
myString = None
# Read and save an integer, double, and String to your variables.
myInt = raw_input()
myFloat = raw_input()
myString = raw_input()

# Print the sum of both integer variables on a new line.
print i + int(myInt)

# Print the sum of the double variables on a new line.
print d + float(myFloat)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
if myString is not None:
    print s+myString
else :
    print s
