class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = set()
        n = len(nums)
        for num in nums:
            if cnt[num] > (n // 3):
                ans.add(num)
        
        return list(ans)
