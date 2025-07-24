# contains_duplicate.py

def containsDuplicate(nums):
    """
    Checks if the input list contains any duplicates.

    Args:
    nums (List[int]): List of integers.

    Returns:
    bool: True if any duplicate exists, False otherwise.
    """

    seen = set()  # Create an empty set to track seen numbers
    
    for num in nums:
        if num in seen:
            # If number already in set, we found a duplicate
            return True
        seen.add(num)  # Otherwise, add number to set
    
    # No duplicates found after checking all numbers
    return False


# Example usage and test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 1], True),
        ([5, 5, 5, 5], True),
        ([], False),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = containsDuplicate(nums)
        print(f"Test case {i}: Input: {nums} -> Contains duplicate? {result} (Expected: {expected})")
