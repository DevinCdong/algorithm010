class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        dp0 = dp1 = 1
        for i, c in enumerate(s):
            if i == 0: continue
            now = dp1
            cprev = s[i - 1]
            if c == '0':
                if not '1' <= cprev <= '2':
                    return 0
                now = dp0
            elif cprev == '1' or ('2' == cprev and '0' <= c <= '6'):
                now += dp0
            dp0, dp1 = dp1, now
        return dp1
