class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            if c not in d:
                return False
            d[c] -= 1
            if d[c] < 0:
                return False
        return True
        
        
        if not len(s) == len(t):
            return False
        ds = {}
        for c in s:
            ds[c] = ds.get(c, 0) + 1
        dt = {}
        for c in t:
            dt[c] = dt.get(c, 0) + 1
        
        for c, cnt in ds.items():
            if c not in dt or cnt != dt[c]:
                return False
        return True
