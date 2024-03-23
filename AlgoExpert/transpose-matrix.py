import program
import unittest
def transposeMatrix(matrix):
    # build transpose skeleton

    transpose =  [[] for _ in range(len(matrix[0]))]

    for array in matrix:
        for idx, elmt in enumerate(array):
            transpose[idx].append(elmt)



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        actual = program.transposeMatrix(input)
        self.assertEqual(actual, expected)
