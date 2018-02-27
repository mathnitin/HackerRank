'''
Day 12: Inheritance

Task 
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has  parameters:
  1. A string, firstName.
  2. A string, lastName.
  3. An integer, id.
  4. An integer array (or vector) of test scores, scores.
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
    
    Grading Scale
   Letter  |  Average (a) 
-----------|----------------
      O    |  90 <= a <= 100
      E    |  80 <= a <  90
      A    |  70 <= a <  80
      P    |  55 <= a <  70
      D    |  40 <= a <  55
      T    |        a <  40


Input Format

The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

You are not responsible for reading the following input from stdin: 
The first line contains firetName, lastName, and id, respectively. The second line contains the number of test scores. The third line of space-separated integers describes scores.

Output Format

This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

Sample Input

Heraldo Memelli 8135627
2
100 80
Sample Output

 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
'''

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber

class Student(Person):

    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate (self):
        total = 0
        for i in self.scores:
            total += i
        a = total/len(self.scores)
        if 90 <= a <= 100:
            return 'O'
        elif 80 <= a <  90:
            return 'E'
        elif 70 <= a <  80:
            return 'A'
        elif 55 <= a <  70:
            return 'P'
        elif 40 <= a <  55:
            return 'D'
        else:
            return 'T'

line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
