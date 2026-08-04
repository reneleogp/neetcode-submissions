class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getHashKey(s):
            hashMap = {}
            for c in s:
                hashMap[c] = hashMap.get(c, 0) + 1
            
            print(hashMap)

            hashKey = ""
            c = 'a'
            while c <= 'z':
                print(c)
                if c in hashMap:
                    hashKey += c + str(hashMap[c])
                c = chr(ord(c) + 1)
            return hashKey
        
        ansMp = {}
        for s in strs:
            hashKey = getHashKey(s)
            ansMp[hashKey] = ansMp.get(hashKey, [])
            ansMp[hashKey].append(s)
        
        ans = []
        for _, value in ansMp.items():
            ans.append(value)
        return ans
                    

            
             
                
