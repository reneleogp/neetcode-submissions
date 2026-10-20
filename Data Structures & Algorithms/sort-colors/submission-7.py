class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lft, i, rght = 0, 0, len(nums) - 1

        def swap(x, y):
            nums[x], nums[y] = nums[y], nums[x]

        while (i <= rght):
            # If num = 0 then we swap lft and 0, increase lft and check next
            if nums[i] == 0:
                swap(i, lft)
                lft += 1
                i += 1
            # If num = 2 then swap with rght, decrease rght and then we need to check the newly swapped number so dont increase i
            elif nums[i] == 2:
                swap(i, rght)
                rght -= 1
            # increase i
            else:
                i += 1
        



        