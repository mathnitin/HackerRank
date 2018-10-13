#!/bin/python

'''
Day 22: Binary Search Trees

Objective 
Today, we're working with Binary Search Trees (BSTs). Check out the Tutorial tab for learning materials and an instructional video!

Task 
The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer, root, pointing to the root of a binary search tree. Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

Input Format
The locked stub code in your editor reads the following inputs and assembles them into a binary search tree: 
The first line contains an integer, n, denoting the number of nodes in the tree. 
Each of the n subsequent lines contains an integer, data, denoting the value of an element that must be added to the BST.

Output Format
The locked stub code in your editor will print the integer returned by your getHeight function denoting the height of the BST.

Sample Input
7
3
5
2
1
4
6
7

Sample Output
3

Explanation
The input forms the following BST:
        ____3____
        |       |
      __2     __5__
      |      |     |
      1      4     6__
                      |
                      7

The longest root-to-leaf path is shown below:
            3____
                |
                5__
                   |
                   6__
                      |
                      7

There are 4 nodes in this path that are connected by 3 edges, meaning our BST's height = 3. Thus, we print 3 as our answer.
'''

class Node():
    def __init__(self, data):
        self.left = self.right = None
        self.data = data

class BST():
    maxHeight = 0
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root

    def getHeight(self,root):
        if root is None:
            return -1
        lH = self.getHeight(root.left)
        rH = self.getHeight(root.right)
        return max(lH, rH) + 1


T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height
