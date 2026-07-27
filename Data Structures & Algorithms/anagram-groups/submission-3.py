class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for s in strs:
            countString = [0] * 26
            for c in s:
                countString[ord(c) - ord('a')] += 1
            hashKey = (tuple(countString))
            counts[hashKey].append(s)
        
        return [value for _, value in counts.items()]
            
             
                
