class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s) + 1, len(p) + 1
        dp = [[0] * m for _ in range(n)]

        dp[0][0] = 1
        for j in range(1, m):
            if p[j - 1] == "*":
                dp[0][j] = 1
            else:
                break

        for i in range(1, n):
            si = s[i - 1]
            for j in range(1, m):
                pj = p[j - 1]
                if si == pj or pj == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif pj == "*":
                    dp[i][j] = dp[i - 1][j] | dp[i][j - 1]
        return bool(dp[-1][-1])
