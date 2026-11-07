class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid[0])
        n = len(grid)
        visited = [[0] * m for i in range(n)]
        distances = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited[i][j] = 1
        
        while q:
            node = q.popleft()
            for dr, dc in distances:
                i, j = node[0] + dr, node[1] + dc
                if not (0 <= i < n and 0 <= j < m):
                    continue

                if not visited[i][j] and grid[i][j] != -1:
                    grid[i][j] = grid[node[0]][node[1]] + 1
                    visited[i][j] = 1
                    q.append((i, j))
        


            

