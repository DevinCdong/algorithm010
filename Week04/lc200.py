class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(a, b):
            if not (0 <= a < n and 0 <= b < m):
                return
            if grid[a][b] == '1':
                grid[a][b] = 0
                dfs(a - 1, b)
                dfs(a + 1, b)
                dfs(a, b - 1)
                dfs(a, b + 1)

        n = len(grid)
        if n == 0:
            return 0
        m =len(grid[0])
        if m == 0:
            return 0
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res
