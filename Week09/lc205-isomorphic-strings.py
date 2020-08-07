class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        ds, dt = {}, {}
        for i in range(n):
            si, ti = s[i], t[i]
            if ds.get(si, -1) != dt.get(ti, -1):
                return False
            ds[si] = dt[ti] = i
        return True
