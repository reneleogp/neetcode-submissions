class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ppa, spa = [nums[0]] * len(nums), [nums[-1]] * len(nums)
        for i in range(1, len(nums)):
            ppa[i] = ppa[i - 1] * nums[i]
            j = len(nums) - 1 - i
            spa[j] = spa[j + 1] * nums[j]

        ans = []

        for i in range(len(nums)):
            if i == 0:
                ans.append(spa[i + 1])
            elif i == len(nums) - 1:
                ans.append(ppa[i - 1])
            else:
                ans.append(ppa[i - 1] * spa[i + 1])
        return ans
                
            