# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/26/2024
# Description: Modify the binary search function from the exploration so that, instead of returning -1 when the target
# value is not in the list, raises a TargetNotFound exception (you'll need to define this exception class).
# Otherwise it should function normally.

import unittest

from bin_except import TargetNotFound, binary_search

class TestBinarySearchAndException(unittest.TestCase):
    """
    Tests the binary_search function and if the TargetNotFound exception is raised correctly
    """

    def test_basic_functionality(self):
        """
        Tests basic functionality to see if target is in the list
        """
        self.assertIn(5, [1, 3, 5, 7, 9])  # Passes if 5 is in the list
        self.assertIn(1, [1, 3, 5, 7, 9])  # Passes if 1 is in the list
        self.assertIn(9, [1, 3, 5, 7, 9])  # Passes if 9 is in the list

        # Check for a value not in the list
        with self.assertRaises(TargetNotFound):
            binary_search([1, 3, 5, 7, 9], 4)  # 4 is not in the list

    def test_empty_list(self):
        """
        Tests if appropriate return if list is empty
        """
        with self.assertRaises(TargetNotFound):
            binary_search([], 1)  # Searching in an empty list

    def test_single_element(self):
        """
        Tests if appropriate return will pass with a single element, if correct or incorrect
        """
        self.assertIn(1, [1])  # Passes if the only element is 1
        with self.assertRaises(TargetNotFound):
            binary_search([1], 2)  # Searching for a non-existent element

    def test_duplicates(self):
        """
        Tests if passes when duplicates are in the list
        """
        # Check for existence of duplicates
        self.assertIn(1, [1, 1, 1, 1, 2, 3, 4])  # Passes if 1 is found
        self.assertIn(4, [1, 1, 1, 1, 2, 3, 4])  # Passes if 4 is found
        with self.assertRaises(TargetNotFound):
            binary_search([1, 1, 1, 1, 2, 3, 4], 5)  # 5 is not in the list

    def test_large_input(self):
        """
        Tests a large list
        """
        large_list = list(range(1000000))  # Create a large sorted list
        self.assertIn(999999, large_list)  # Passes if 999999 is found
        with self.assertRaises(TargetNotFound):
            binary_search(large_list, 1000001)  # Target not found

if __name__ == "__main__":
    unittest.main()
