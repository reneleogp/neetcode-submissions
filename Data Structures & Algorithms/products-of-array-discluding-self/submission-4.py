class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(ans[i - 1] * nums[i])
        
        suffixProduct = 1
        for i in range(len(nums) - 1, 0, -1): # we skip 0 here
            ans[i] = suffixProduct * ans[i - 1]
            suffixProduct *= nums[i]
        ans[0] = suffixProduct
        return ans
                
            