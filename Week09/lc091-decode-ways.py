class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        if s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * n
        for i, c in enumerate(s):
            if c == "0":
                sim1 = s[i - 1]
                if sim1 == "1" or sim1 == "2":
                    dp[i] = dp[i - 2] if i >= 2 else 1
                else:
                    return 0
            else:
                dp[i] += dp[i - 1] if i >= 1 else 1
                if i >= 1:
                    sim1 = s[i - 1]
                    if (sim1 == "1" and "0" <= c <= "9") or \
                        (sim1 == "2" and "0" <= c <= "6"):
                        dp[i] += dp[i - 2] if i >= 2 else 1
        return dp[-1]
