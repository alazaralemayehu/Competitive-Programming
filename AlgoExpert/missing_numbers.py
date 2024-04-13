import unittest

def missingNumbers(nums):
    # Write your code here.
    length = len(nums)
    missing_element = []
    nums_set = set(nums)
    for nums in range(1, length + 3):
        if not nums in nums_set:
            missing_element.append(nums)
    return missing_element


class TestTransposeMatrix(unittest.TestCase):
    def test_case_1(self):
        input = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        expected = [1, 2]
        actual = missingNumbers(input)
        self.assertEqual(actual, expected)
