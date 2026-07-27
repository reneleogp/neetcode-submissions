class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        counts = {}

        def getHashKey(countS):
            currLetterNum = ord('a')
            hashKey = ''
            while currLetterNum <= ord('z'):
                currLetter = chr(currLetterNum)
                val = countS.get(currLetter, 0)
                hashKey += currLetter + str(val)

                currLetterNum += 1
            return hashKey


        for s in strs:
            
            
            countString = {}
            for c in s:
                countString[c] = countString.get(c, 0) + 1
            hashKey = getHashKey(countString)
            counts[hashKey] = counts.get(hashKey, [])
            counts[hashKey].append(s)
        
        return [value for _, value in counts.items()]
            
             
                
