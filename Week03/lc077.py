class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(begin, cur):
            if len(cur) == k:
                res.append(cur[:])
                return
            m = n - (k - len(cur)) + 1
            for i in range(begin, m):
                cur.append(i + 1)
                dfs(i + 1, cur)
                cur.pop()
        res = []
        dfs(0, [])
        return res
