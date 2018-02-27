'''
Day 2 - Operators
Input Format

There are  lines of numeric input: 
The first line has a double, mealCost (the cost of the meal before tax and tip). 
The second line has an integer, tipPercent (the percentage of  being added as tip). 
The third line has an integer, taxPercent (the percentage of  being added as tax).

Output Format

Print The total meal cost is totalCost dollars., where totalCost is the rounded integer result of the entire bill ( mealCost with added tax and tip).

Sample Input

12.00
20
8
Sample Output

The total meal cost is 15 dollars.
'''
#!/bin/python

import sys

if __name__ == "__main__":
    meal_cost = float(raw_input().strip())
    tip_percent = int(raw_input().strip())
    tax_percent = int(raw_input().strip())
    if tip_percent > 0:
                tip = float((float(meal_cost)*float(tip_percent)/100))
    if tax_percent > 0:
                tax = float((float(meal_cost)*float(tax_percent)/100))
    totalCost = meal_cost + tip + tax
    print 'The total meal cost is', int(round(totalCost)), 'dollars.'
