from typing import List

def smallest_missing_positive_integer(nums: List[int]) -> int:
    """
    Find the smallest missing positive integer in the given list.

    Args:
    nums: An unsorted list of integers.

    Returns:
    The smallest missing positive integer.
    """
    n = len(nums)
    
    # Perform cyclic sort to place each number at its correct index
    i = 0
    while i < n:
        if 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        else:
            i += 1
    
    # Iterate through the sorted array to find the smallest missing positive integer
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    # If all positive integers from 1 to n are present, return n + 1
    return n + 1

# Test cases
print(smallest_missing_positive_integer([3, 4, -1, 1]))  
print(smallest_missing_positive_integer([1, 2, 0]))     
print(smallest_missing_positive_integer([-1, -3, 4, 2])) 




    



  

