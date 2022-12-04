# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root):
    node_depth = 0

    node_depth = nodeDepthHelper(root, node_depth)

    return node_depth


def nodeDepthHelper(root, depth):
    if root is None:
        return 0
    return (
        depth
        + nodeDepthHelper(root.left, depth + 1)
        + nodeDepthHelper(root.right, depth + 1)
    )

    return depth


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(9)
        root.left.right = BinaryTree(5)
        root.right = BinaryTree(3)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        actual = nodeDepths(root)
        self.assertEqual(actual, 16)


t = TestProgram()
t.test_case_1()
