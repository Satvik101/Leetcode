from typing import List

class Solution:
    """
    Two Sum Problem Solutions
    
    Problem:
        Given an array of integers `nums` and an integer `target`,
        return indices of the two numbers such that they add up to the target.

    Constraints:
        - Exactly one solution exists.
        - You cannot use the same element twice.
        - Return the answer in any order.
    """

    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
        """
        Brute Force Approach:
            - Check every pair of numbers to find the two that add up to the target.
            - Time Complexity: O(n^2)
            - Space Complexity: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        # If no solution found (per problem statement, this should never happen)
        return []

    def twoSum_optimized(self, nums: List[int], target: int) -> List[int]:
        """
        Optimized Approach Using Hash Map (Dictionary):
            - Iterate once through the list.
            - For each number, check if its complement (target - num) is already in the dictionary.
            - If yes, return indices.
            - Otherwise, store the current number and index in the dictionary.
            - Time Complexity: O(n)
            - Space Complexity: O(n)
        """
        seen = {}  # Maps number -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []  # If no solution found (should not happen)


if __name__ == "__main__":
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    # Using brute force
    result_brute = solution.twoSum_brute_force(nums, target)
    print("Brute force result:", result_brute)

    # Using optimized approach
    result_optimized = solution.twoSum_optimized(nums, target)
    print("Optimized result:", result_optimized)
