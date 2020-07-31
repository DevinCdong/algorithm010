class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(ll, rr, cc, cnt):
            if cnt == n:
                self.res += 1
                return
            used = ll | rr | cc
            for i in range(n):
                fi = 1 << i
                if fi & used:
                    continue
                dfs(((ll | fi) << 1) & maxv, (rr | fi) >> 1, cc | fi, cnt + 1)

        maxv = (1 << n) - 1
        self.res = 0
        dfs(0, 0, 0, 0)
        return self.res
