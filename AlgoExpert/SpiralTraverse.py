import unittest

def spiralTraverse(array):
    min_col, min_row, max_col, max_row = 0,0, len(array[0])-1, len(array)-1
    traversed_array = []

    while min_col <= max_col and min_row <= max_row:
        for col in range(min_col, max_col+1):
            traversed_array.append(array[min_row][col])
        
        for row in range(min_row+1, max_row + 1):
            traversed_array.append(array[row][max_col])
        
        for col in range(max_col-1, min_col-1, -1):
            if min_row == max_row:
                break
            traversed_array.append(array[max_row][col])
        
        for row in range(max_row - 1, min_row, -1):
            if min_col == max_col:
                break
            traversed_array.append(array[row][min_col])
        
        min_col +=1
        max_col -=1
        min_row +=1
        max_row -=1
    return traversed_array


    




class TestSpiralTraverse(unittest.TestCase):
    def test_case_1(self):
        # matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        matrix = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
  ]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        actual = spiralTraverse(matrix)
        print(actual)
        self.assertEqual(actual, expected)
