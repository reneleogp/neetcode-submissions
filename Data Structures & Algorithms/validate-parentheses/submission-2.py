class Solution:
    def isValid(self, s: str) -> bool:
        current = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                current.append(c)
                continue
            if not current:
                return False
            elif c == ')':
                a = current.pop()
                if a != '(':
                    return False
            elif c == '}':
                a = current.pop()
                if a != '{':
                    return False
            elif c == ']':
                a = current.pop()
                if a != '[':
                    return False

        
        return not current