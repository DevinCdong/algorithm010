学习笔记

不同路径 2 的状态转移方程
if G[i][j] == 1:
    dp[i][j] = 0
elif j > 0:
    dp[i][j] = (dp[i - 1][j] if i > 0 else 0) + (dp[i][j - 1] if j > 0 else 0)
