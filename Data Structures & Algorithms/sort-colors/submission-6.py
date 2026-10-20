class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lft, i, rght = 0, 0, len(nums) - 1

        def swap(x, y):
            nums[x], nums[y] = nums[y], nums[x]

        while (i <= rght):
            if nums[i] == 0:
                swap(i, lft)
                lft += 1
                i += 1
            elif nums[i] == 2:
                swap(i, rght)
                rght -= 1
            else:
                i += 1
        



        