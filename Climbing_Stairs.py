class Solution:
    def climbStairs(self, n: int) -> int:
        # If there are 1 or 2 stairs, the number of ways to climb is n itself
        if n <= 2:
            return n

        # Initialize base cases:
        # first = ways to climb 1 stair
        # second = ways to climb 2 stairs
        first, second = 1, 2

        # For stairs from 3 to n, calculate the number of ways iteratively
        for _ in range(3, n + 1):
            # Current number of ways is sum of the previous two
            first, second = second, first + second

        # After the loop, 'second' holds the total number of ways to climb n stairs
        return second

if __name__ == "__main__":
    solution = Solution()
    n = int(input("Enter number of stairs: "))
    result = solution.climbStairs(n)
    print(f"Number of ways to climb {n} stairs: {result}")



"""
LeetCode Problem: 70. Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs/

Problem:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Approach:
This is a classic dynamic programming problem.
Use two variables to store the number of ways to reach the last two steps,
and build up the solution iteratively.

Time Complexity: O(n)
Space Complexity: O(1)
"""
