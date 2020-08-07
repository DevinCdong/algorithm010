class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s) + 1
        m = len(p) + 1
        dp = [[0] * m for _ in range(n)]

        dp[0][0] = 1
        for j in range(1, m):
            if p[j - 1] == "*":
                if dp[0][j - 2]:
                    dp[0][j] = 1
                else:
                    break

        for i in range(1, n):
            si = s[i - 1]
            for j in range(1, m):
                pj = p[j - 1]
                if si == pj or pj == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif pj == "*":
                    pjm1 = p[j - 2]
                    val = dp[i][j - 2]
                    if si == pjm1 or pjm1 == ".":
                        val |= dp[i - 1][j] | dp[i][j - 1]
                    dp[i][j] = val
        return bool(dp[-1][-1])
