class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Interger array prices, with price of a stock on ith day
        # can sell or buy stock each day, can buy and sell same day
        # can perform any number of transactions, can hold only one share at a time

        # Example: [7, 1, 5, 3, 6, 4]
        # 3 * 1e4
        dp = [0] * (len(prices) + 1)

        for i in range(len(prices) - 1, -1, -1):
            profit = 0
            # Buy at i
            for j in range(i + 1, len(prices)):
                # sell if possible, then profit is selling at that day and possible profit buying the day after
                if prices[j] > prices[i]:
                    profit = max(profit, prices[j] - prices[i] + dp[j + 1])
            dp[i] = max(profit, dp[i + 1])
        return dp[0]



