class Solution:
    # Takes two sorted arrays and arranges them
    def merge(self, start1, end1, start2, end2, nums):
        i, j = start1, start2
        ans = []
        while (i <= end1 or j <= end2):
            # Case 1: first array allocated
            if (i > end1):
                ans.append(nums[j])
                j += 1
            # Case 2: Second array allocated
            elif (j > end2):
                ans.append(nums[i])
                i += 1
            # Case 3: first num of arr1 is smaller than first of arr2
            elif (nums[i] < nums[j]):
                ans.append(nums[i])
                i += 1
            # Case 4: First num of arr2 is smaller
            else:
                ans.append(nums[j])
                j += 1
        for k in range(len(ans)):
            nums[start1 + k] = ans[k]

            
    # Takes a chunk of an array and sorts it
    def mergeSort(self, nums, start, end):
        # If the chunk has lenght 1 then is sorted
        if (end - start <= 0):
            return

        # Otherwise we divide the array into two pieces and we sort each piece
        end1 = (start + end) // 2
        start2 = end1 + 1
        self.mergeSort(nums, start, end1)
        self.mergeSort(nums, start2, end)
        # We merge the two sorted pieces
        self.merge(start, end1, start2, end, nums)


    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0,  len(nums) - 1)
        return nums
