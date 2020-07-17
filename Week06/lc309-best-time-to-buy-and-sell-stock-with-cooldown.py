class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        dp0 = [0] * n
        dp1 = [0] * n
        dp1[0] = -prices[0]
        for i in range(1, n):
            pi = prices[i]
            dp0[i] = max(dp0[i - 1], dp1[i - 1] + pi)
            dp1[i] = max((dp0[i - 2] if i >= 2 else 0) - pi, dp1[i - 1])
        return dp0[-1]
