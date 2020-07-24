class Solution:
    dxy = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1 or n == 0: return -1
        import heapq as hh
        heap = [(n - 1, 1, 0, 0)]
        dist = {0: 1}
        visit = set()
        maxv = int(1e9)
        while heap:
            f, d, i, j = hh.heappop(heap)
            if i == n - 1 and j == n - 1:
                return d
            node = (i, j)
            if node in visit:
                continue
            visit.add(node)

            for x, y in self.dxy:
                ii, jj = i + x, j + y
                if not (0 <= ii < n and 0 <= jj < n and grid[ii][jj] == 0):
                    continue
                sub = (ii, jj)
                if sub in visit:
                    continue
                if dist.get(sub, maxv) > d + 1:
                    heu = d + 1 + max(n - ii, n - jj)
                    # heu = d + 1     把上面一行注释掉，换成这行，仍旧可以通过，但时间翻倍
                    # heu = d + 1 + (n - ii + n - jj)       不通过
                    # heu = max(n - ii, n - jj)     不通过
                    hh.heappush(heap, (heu, d + 1, ii, jj))
                    dist[sub] = d + 1
        return -1
