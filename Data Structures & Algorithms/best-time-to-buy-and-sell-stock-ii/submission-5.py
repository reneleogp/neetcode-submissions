class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Interger array prices, with price of a stock on ith day
        # can sell or buy stock each day, can buy and sell same day
        # can perform any number of transactions, can hold only one share at a time

        # Example: [7, 1, 5, 3, 6, 4]
        # 3 * 1e4
        dp = [0] * (len(prices) + 1)

        for i in range(len(prices) - 2, -1, -1):
            dp[i] = dp[i + 1] + max(0, prices[i + 1] - prices[i])
        return dp[0]