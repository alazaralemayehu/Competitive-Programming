# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne: LinkedList, linkedListTwo: LinkedList):
    # Write your code here.
    linked_list: LinkedList = LinkedList(0)
    linked_list_backup = linked_list
    str1 = ""
    str2 = ""
    while linkedListOne.next:
        str1 += str(linkedListOne.value)
        linkedListOne = linkedListOne.next
    while linkedListTwo.next:
        str2 += str(linkedListTwo.value)
        linkedListTwo = linkedListTwo.next
    str1 += str(linkedListOne.value)
    str2 += str(linkedListTwo.value)
    summation = int(str1[::-1]) + int(str2[::-1])
    while summation > 0:
        remainder = summation % 10
        summation = summation // 10
        ll = LinkedList(remainder)

        linked_list_backup.next = ll
        linked_list_backup = linked_list_backup.next

    return linked_list.next


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self


def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        ll1 = LinkedList(2).addMany([4, 7, 1])
        ll2 = LinkedList(9).addMany([4, 5])
        expected = LinkedList(1).addMany([9, 2, 2])
        actual = sumOfLinkedLists(ll1, ll2)
        self.assertEqual(getNodesInArray(actual), getNodesInArray(expected))


t = TestProgram()
t.test_case_1()
