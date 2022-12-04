class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inOrderTraverse(tree: BST, array: list):
    # Write your code here.

    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)

    return array


def preOrderTraverse(tree, array):
    # Write your code here.
    if tree is not None:
        array.append(tree.value, array)
        preOrderTraverse(tree, array)
        preOrderTraverse(tree.right, array)

    return array


def postOrderTraverse(tree, array):
    # Write your code here.
    if tree is not None:
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
        postOrderTraverse(tree.left, array)

    return array
