class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(ans[i - 1] * nums[i])
        
        suffixProduct = 1
        # we skip 0 here
        for i in range(len(nums) - 1, 0, -1):
            ans[i] = suffixProduct * ans[i - 1]
            suffixProduct *= nums[i]
        
        # Set the first element to be the suffixProduct
        ans[0] = suffixProduct
        return ans
                
            