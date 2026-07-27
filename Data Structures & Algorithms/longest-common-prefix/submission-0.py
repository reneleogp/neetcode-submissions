class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur = ""
        for i in range(len(strs[0])):
            current_char = strs[0][i]
            for s in strs:
                if i < len(s) and s[i] == current_char:
                    continue
                return cur
            
            cur += current_char
        
        return cur
