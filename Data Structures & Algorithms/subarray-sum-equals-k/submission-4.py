class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cntSum = {}
        currentSum = 0
        cntSum[0] = 1
        for i in range(len(nums)):
            currentSum += nums[i]
            lookingFor = currentSum - k
            cnt = cntSum.get(lookingFor, 0)
            ans += cnt
            cntSum[currentSum] = cntSum.get(currentSum, 0) + 1
            
            
        return ans