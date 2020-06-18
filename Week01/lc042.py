class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        n = len(h)
        if n <= 2: return 0
        l, r = 0, n - 1
        lm = rm = 0
        res = 0
        while l < r:
            lm = max(lm, h[l])
            rm = max(rm, h[r])
            if lm <= rm:
                res += lm - h[l]
                l += 1
            else:
                res += rm - h[r]
                r -= 1
        return res
