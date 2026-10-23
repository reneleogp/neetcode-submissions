class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psa = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            psa[i + 1] = psa[i] + nums[i]

        ans = 0
        cntSum = {}
        cntSum[0] = 1
        for i in range(len(nums)):
            lookingFor = psa[i + 1] - k
            cnt = cntSum.get(lookingFor, 0)
            ans += cnt
            cntSum[psa[i + 1]] = cntSum.get(psa[i + 1], 0) + 1
            
        return ans