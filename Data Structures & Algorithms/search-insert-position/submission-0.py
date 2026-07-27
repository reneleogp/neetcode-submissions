class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        lft, rght = 0, len(nums) - 1

        while lft <= rght:
            mid = (lft + rght) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lft = mid + 1
            else:
                rght = mid - 1
        
        return lft

            