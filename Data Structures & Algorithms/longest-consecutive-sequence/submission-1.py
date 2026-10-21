class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        present = set(nums)

        for num in present:
            # check if the number is a starter of a sequence by checking if it has a previous one
            if (num - 1) not in present:
                # find the length of the sequence
                length = 1
                while num + length in present:
                    length += 1
                ans = max(ans, length)


        return ans
        



            