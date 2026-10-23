class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Interger array prices, with price of a stock on ith day
        # can sell or buy stock each day, can buy and sell same day
        # can perform any number of transactions, can hold only one share at a time

        # Example: [7, 1, 5, 3, 6, 4]
        # 3 * 1e4
        ans = 0
        for i in range(1, len(prices)):
            ans += max(0, prices[i] - prices[i - 1])
        return ans