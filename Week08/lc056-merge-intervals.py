class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        l = r = 0
        arr = intervals
        arr.sort()
        n = len(arr)
        while l < n:
            ll, lr = arr[l]
            r = l + 1
            while r < n:
                rl, rr = arr[r]
                if rl <= lr:
                    lr = max(lr, rr)
                else:
                    break
                r += 1
            l = r
            res.append((ll, lr))
        return res
