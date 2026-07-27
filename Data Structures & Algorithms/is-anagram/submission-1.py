class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        countS = {}

        for c in s:
            countS[c] = countS.get(c, 0) + 1
        
        for c in t:
            countS[c] = countS.get(c, 0) - 1
            if countS[c] < 0:
                return False

        return True
            
        
        
        


        