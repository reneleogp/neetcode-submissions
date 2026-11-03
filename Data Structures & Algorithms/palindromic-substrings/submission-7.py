class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)
        
        def expand(i, j):
            nonlocal cnt, n
            while i >= 0 and j < n and s[i] == s[j]:
                cnt += 1
                i -= 1
                j += 1
                
        for center in range(n):
            expand(center, center)
            expand(center, center + 1)

        return cnt
