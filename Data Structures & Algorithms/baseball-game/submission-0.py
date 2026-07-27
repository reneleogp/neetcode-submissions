class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for c in operations:
            if c == '+':
                a = record[-1]
                b = record[-2]
                record.append(a + b)
            elif c == 'D':
                record.append(record[-1] * 2)
            elif c == 'C':
                record.pop()
            else:
                record.append(int(c))

        return(sum(record))