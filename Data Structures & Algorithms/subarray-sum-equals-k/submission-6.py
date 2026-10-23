class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        currentSum = 0
        cntSum = {0: 1}
        for num in nums:
            currentSum += num
            lookingFor = currentSum - k
            ans += cntSum.get(lookingFor, 0)
            cntSum[currentSum] = cntSum.get(currentSum, 0) + 1
             
        return ans