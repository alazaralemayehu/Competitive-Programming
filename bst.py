# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
import pytest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if self.value >= value:
            if self.right is None:
                bst = BST(value)
                self.right = bst
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                bst = BST(value)
                self.left = bst
            else:
                self.left.insert(value)
        return self

    def contains(self, value):
        # Write your code here.
        if self.value is value:
            return True

        if value > self.value:
            if self.right == None:
                return False
            return self.right.contains(value)

        if value < self.value:
            if self.left == None:
                return False

            return self.left.contains(value)

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.

        return self


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!


def test_bst():
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)

    root.insert(10)
    print(root.contains(12))
    print(root.right.left.left.value)


test_bst()
# self.assertTrue(root.right.left.left.value == 12)

# root.remove(10)
# self.assertTrue(not root.contains(10))
# self.assertTrue(root.value == 12)

# self.assertTrue(root.contains(15))
