class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_l, ans_r = 0, 0

        def expand(l, r):
            nonlocal ans_l, ans_r
            while (l >= 0 and r < n and s[l] == s[r]):
                l -= 1
                r += 1
            if ans_r - ans_l < (r - 1) - (l + 1):
                ans_l = l + 1
                ans_r = r - 1



        for i in range(n): 
            # Case 1: i is center
            l = i - 1
            r = i + 1
            expand(l, r)
            
            # Case 2: i and i + 1 are center
            l = i
            r = i + 1
            expand(l, r)
            

        return s[ans_l:ans_r + 1]