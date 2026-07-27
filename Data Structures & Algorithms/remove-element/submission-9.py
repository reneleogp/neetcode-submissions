class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lft = 0
        rght = len(nums)

        while lft < rght:
            if nums[lft] == val:
                rght -= 1
                nums[lft], nums[rght] = nums[rght], nums[lft]
            else:
                lft += 1

        return rght

                
            

