class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        t = {}
        for c in p:
            t[c] = t.get(c, 0) + 1
        
        k = len(p)
        hit = 0
        res = []
        for r, c in enumerate(s):
            t[c] = t.get(c, 0) - 1
            if t[c] >= 0:
                hit += 1
            if r >= k:
                sl = s[r - k]
                t[sl] += 1
                if t[sl] > 0:
                    hit -= 1
            if hit == k:
                res.append(r - k + 1)
        return res
