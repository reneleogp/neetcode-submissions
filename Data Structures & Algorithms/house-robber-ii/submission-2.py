class Solution:
    def rob(self, nums: List[int]) -> int:
        def sub_rob(sub_nums):
            if not sub_nums:
                return 0
            
            n = len(sub_nums)
            dp = [0] * (n + 1)
            dp[1] = sub_nums[0]
            for i in range(2, n + 1):
                dp[i] = max(sub_nums[i - 1] + dp[i - 2], dp[i - 1])
        
            return dp[n]

        if len(nums) == 1:
            return nums[0]
        
        return max(sub_rob(nums[1:]),
                    sub_rob(nums[:-1]),
        )
        

        