"""This is a test module to check edge cases for the median function"""

from typing import List


# Edge Case 1: Empty List
edge_case_1 = []

def test_get_median(edge_case) -> List:
    """
    Tests the get_median function against edge cases
    
    Arg:
    edge case 1: empty list
    edge case 2: out of order list with an odd amount of values
    edge case 3: ordered list with an even amount of values
    
    Return:
    If all tests pass -> "All Tests Passed"
    If tests failed -> "X Tests Failed"
    """
    
