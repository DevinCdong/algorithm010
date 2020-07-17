class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        maxv = int(1e9)
        
        dp = [0] * m
        for i in range(n):
            for j in range(m):
                up = dp[j] if i > 0 else 1e9
                lf = dp[j - 1] if j > 0 else dp[0]
                dp[j] = min(up, lf) + grid[i][j]
        return dp[-1]

        dp = [maxv] * m
        dp[0] = 0
        for i in range(n):
            for j in range(m):
                gij = grid[i][j]
                if j == 0:
                    dp[0] += gij
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + gij
        return dp[-1]
