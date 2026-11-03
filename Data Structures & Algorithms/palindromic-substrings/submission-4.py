class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        for size in range(1, n + 1):
            for i in range(n):
                j = i + (size - 1)
                if j >= n:
                    break
                if size == 1:
                    dp[i][j] = 1
                elif size == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])                    
                if dp[i][j]:
                    cnt += 1
        return cnt
