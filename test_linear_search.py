import unittest
from main import linear_search

class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        # Test when target is in the array
        arr1 = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(arr1, 3), 2)

        # Test when target is not in the array
        arr2 = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(arr2, 6), -1)

        # Test when array is empty
        arr3 = []
        self.assertEqual(linear_search(arr3, 1), -1)

        # Test when array has only one element
        arr4 = [5]
        self.assertEqual(linear_search(arr4, 5), 0)

if __name__ == '__main__':
    unittest.main()

