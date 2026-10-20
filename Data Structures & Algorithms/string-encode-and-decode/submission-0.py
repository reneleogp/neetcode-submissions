class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            sz = len(s)
            ans += str(sz) + '#' + s
        
        print(ans)
        return ans
        

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            # find the number and the start of the string
            sz_str = ""
            while s[i] != "#":
                sz_str += s[i]
                i += 1
            i += 1
            sz = int(sz_str)
            
            # find the string
            cur = ""

            for j in range(i, i + sz):
                cur += s[j]
            
            i = i + sz

            # append the string to the answer

            ans.append(cur)
        return ans
            
            


