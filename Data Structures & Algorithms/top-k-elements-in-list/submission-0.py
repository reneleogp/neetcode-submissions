class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1e4
        

        # First we are going to count with a Hashmap how many numbers are there of each
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        # Then we are going to sort the pairs by the value
        counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        
        ans = [counter[i][0] for i in range(k)]

        # Then we select the top k elements
        return ans