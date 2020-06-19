class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        import heapq as hh
        h = list((-v, k) for k, v in c.items())
        hh.heapify(h)
        res = []
        for i in range(k):
            res.append(hh.heappop(h)[1])
        return res
