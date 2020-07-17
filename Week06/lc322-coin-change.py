class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(cid, cnt, rem):
            if rem == 0 and cnt < self.res: 
                self.res = cnt
                return
            if cid >= len(coins):
                return 
            coin = coins[cid]
            k = rem // coin
            while k >= 0:
                if cnt + k > self.res: return
                dfs(cid + 1, cnt + k, rem - k * coin)
                k -= 1
        
        coins.sort(reverse=True)
        if amount == 0: return 0
        self.res = 1e10
        dfs(0, 0, amount)
        return self.res if self.res < 1e10 else -1


        n = amount + 1
        dp = [n] * n
        dp[0] = 0
        for i in range(n):
            for c in coins:
                ic = i - c
                if ic >= 0:
                    dp[i] = min(dp[i], dp[ic] + 1)
        r = dp[-1]
        return r if r < n else -1
