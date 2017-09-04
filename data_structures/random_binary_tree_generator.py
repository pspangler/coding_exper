#!/usr/bin/python
""" Python version of the Random Binary Tree generator code in
    Jonathan's handout.

    https://www.meetup.com/tech-interviews-and-competitive-programming/events/242986801/
"""

from random import random

class Node(object):
    """ A simple binary tree node. """
    def __init__(self):
        self.left = None
        self.right = None
        self.data = 0

    def add_child_node(self, new_node, treeside):
        """ Add a new child node this node. treeside should be 'left' or 'right' """
        if treeside == 'left':
            self.left = new_node
        else:
            self.right = new_node

    def get_data(self):
        """ getter method """
        return self.data

    def set_data(self, new_data_val):
        """ setter method """
        self.data = new_data_val

def make_random_tree(node, depth):
    """ Given a root node and a specified tree depth, build a
        binary tree with random integer values.
    """
    # randomValue is an integer
    random_value = random() * 20
    node.data = "" + str(random_value)
    # maxDepth is likewise an integer
    max_depth = (2 + random() * 3)

    # Stop when we get deep enough. (our halt condition)
    if depth > max_depth:
        return

    node.left = Node()
    node.right = Node()
    make_random_tree(node.left, depth + 1)
    make_random_tree(node.right, depth + 1)


#
# @param node  Node
# @param depth integer
#
def print_tree(node, depth):
    """ recursively print the tree """
    if node is None:
        return

    outstring = ""
    for i in range(0, depth):
        if i == (depth-1):
            outstring += "|_____"
        else:
            outstring += "      "

    print " " + outstring + str(node.data)
    print_tree(node.left, depth + 1)
    print_tree(node.right, depth + 1)


def main():
    """ Our simple main function """
    root_node = Node()
    make_random_tree(root_node, 0)
    print_tree(root_node, 0)


main()
