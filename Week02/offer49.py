class Solution:
    import heapq as hh
    h = [1]
    cache = []
    t = set()
    for i in range(1690):
        n = hh.heappop(h)
        cache.append(n)
        for x in (2, 3, 5):
            nx = n * x
            if nx not in t:
                t.add(nx)
                hh.heappush(h, nx)
    def nthUglyNumber(self, n: int) -> int:
        return self.cache[n - 1]

