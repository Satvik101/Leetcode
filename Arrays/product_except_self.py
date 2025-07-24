# product_except_self.py

def productExceptSelf(nums):
    """
    Given an integer array nums, return an array answer such that
    answer[i] is equal to the product of all the elements of nums except nums[i].

    This is done without using division and in O(n) time.

    Args:
    nums (List[int]): List of integers.

    Returns:
    List[int]: Product array as described above.
    """

    n = len(nums)
    answer = [1] * n  # Initialize the result array with 1s

    # Step 1: Calculate prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Step 2: Calculate suffix products and multiply with prefix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


# Example usage and test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([0, 0], [0, 0]),
        ([1, 0], [0, 1]),
        ([2, 3, 4, 5], [60, 40, 30, 24]),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = productExceptSelf(nums)
        print(f"Test case {i}: Input: {nums} -> Output: {result} (Expected: {expected})")
