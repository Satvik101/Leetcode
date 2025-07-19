from typing import List

class Solution:
    """
    LeetCode Problem: Best Time to Buy and Sell Stock
    --------------------------------------------------
    You are given an array 'prices' where prices[i] is the price of a given stock on the i-th day.

    You want to maximize your profit by choosing a single day to buy one stock 
    and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. 
    If you cannot achieve any profit, return 0.

    Example:
        Input: prices = [7, 1, 5, 3, 6, 4]
        Output: 5
        Explanation: Buy on day 1 (price = 1) and sell on day 4 (price = 6), profit = 6 - 1 = 5.
                     You cannot sell before you buy.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')   # Initialize to a very high value
        max_profit = 0             # No profit initially

        for price in prices:
            if price < min_price:
                # Found a new lower buying price
                min_price = price
            else:
                # Calculate profit if we sold at current price
                profit = price - min_price
                max_profit = max(max_profit, profit)  # Update max profit if it's higher

        return max_profit


if __name__ == "__main__":
    # Example usage
    solution = Solution()

    # Test case
    prices = [7, 1, 5, 3, 6, 4]
    result = solution.maxProfit(prices)

    print("Prices:", prices)
    print("Maximum Profit:", result)  # Expected output: 5
