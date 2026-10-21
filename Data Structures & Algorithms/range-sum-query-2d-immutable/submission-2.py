class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # We initialize by creating a Matrix sum. This matrix sum will be as follows
        # Each square represents the sum of elements with upper right corner 0, 0
        # and lower right corner i, j

        self.matrixSum = []
        self.matrixSum.append([0] * (len(matrix[0]) + 1))
        for i in range(1, len(matrix) + 1):
            self.matrixSum.append([])
            self.matrixSum[i].append(0)

            for j in range(1, len(matrix[i - 1]) + 1):
                self.matrixSum[i].append(
                    matrix[i - 1][j - 1] + 
                    self.matrixSum[i][j-1] + 
                    self.matrixSum[i-1][j] - 
                    self.matrixSum[i-1][j-1])


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrixSum[row2 + 1][col2 + 1] - self.matrixSum[row2 + 1][col1] - self.matrixSum[row1][col2 + 1] + self.matrixSum[row1][col1]

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)