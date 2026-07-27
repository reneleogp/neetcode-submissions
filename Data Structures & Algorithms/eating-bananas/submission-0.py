class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxElement = max(piles)
        ans = maxElement
        lft, rght = 1, maxElement

        while lft <= rght:
            k = (lft + rght) // 2
            
            # try with the k
            current_h = 0
            for num in piles:
                current_h += num // k
                if num % k != 0:
                    current_h += 1
            
            if current_h > h:
                lft = k + 1
            else:
                ans = min(k, ans)
                rght = k - 1
        
        return ans    