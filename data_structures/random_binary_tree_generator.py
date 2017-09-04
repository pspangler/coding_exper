#!/usr/bin/python
#Python version of the Random Binary Tree generator code in
#    Jonathan's handout.
#
#    https://www.meetup.com/tech-interviews-and-competitive-programming/events/242986801/
#

from random import random

class Node:
	def __init__(self):
         self.left = None
         self.right = None
         self.data = 0

def makeRandomTree(node, depth):
   # randomValue is an integer
   randomValue = random() * 20
   node.data = "" + str(randomValue);
   # maxDepth is likewise an integer
   maxDepth = (2 + random() * 3)

   # Stop when we get deep enough. (our halt condition)
   if depth > maxDepth:
       return

   node.left = Node()
   node.right = Node()
   makeRandomTree(node.left, depth + 1)
   makeRandomTree(node.right, depth + 1)


# 
# @param node  Node
# @param depth integer
# 
def printTree(node, depth):
    if node is None:
    	return

    outstring = ""
    for i in range(0, depth):
        if i == (depth-1):
            outstring += "|_____"
        else:
            outstring += "      "

    print " " + outstring + str(node.data)
    printTree(node.left, depth + 1)
    printTree(node.right, depth + 1)


def main():
    rootNode = Node()
    makeRandomTree(rootNode, 0)
    printTree(rootNode, 0)


main()