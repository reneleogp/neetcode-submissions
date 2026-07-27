class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        firstValPos = -1

        for i in range(len(nums)):
            if nums[i] == val and firstValPos == -1:
                firstValPos = i

            if nums[i] != val and firstValPos != -1 and i > firstValPos:
                nums[i], nums[firstValPos] = nums[firstValPos], nums[i]
                firstValPos += 1

                while nums[firstValPos] != val:
                    firstValPos += 1
        
        return firstValPos if firstValPos != -1 else len(nums)                

                
            

