class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ansMp = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            ansMp[key].append(s)
        
        ans = []
        for _, value in ansMp.items():
            ans.append(value)
        return ans
                    

            
             
                
