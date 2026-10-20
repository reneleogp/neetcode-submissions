class Solution:
    # moves all the numbers = x to the start, returns the end
    def moveFront(self, nums, x, start) -> int:
        lft = start
        # lft contains the last number that is not an x
        for i in range(start, len(nums)):
            # check if number we are looking at is X, if so swap with last non x
            if (nums[i] == x):
                nums[i], nums[lft] = nums[lft], nums[i]
                lft += 1

        return lft
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = self.moveFront(nums, 0, 0)
        start = self.moveFront(nums, 1, start)
        start = self.moveFront(nums, 2, start)



        