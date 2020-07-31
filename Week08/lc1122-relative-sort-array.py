class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        t = dict((x, i) for i, x in enumerate(arr2))
        arr1.sort(key = lambda x: t[x] if x in t else 10000 + x)
        return arr1
    
    
    
        cnt = [0] * 1001
        for x in arr1:
            cnt[x] += 1
        res = []
        for y in arr2:
            while cnt[y] > 0:
                cnt[y] -= 1
                res.append(y)
        for i, x in enmuerate(cnt):
            while x > 0:
                x -= 1
                res.append(i)
        return res
