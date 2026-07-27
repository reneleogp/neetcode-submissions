class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        cnt = 0
        visited = set()
        def visit(i, j):
            nonlocal cnt, visited
            if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0:
                return
            if grid[i][j] == 0:
                return
            if (i, j) in visited:
                return
            visited.add((i, j))
            cnt += 1
            visit(i + 1, j)
            visit(i - 1, j)
            visit(i, j + 1)
            visit(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                visit(i, j)
                ans = max(ans, cnt)
                cnt = 0

        return ans
