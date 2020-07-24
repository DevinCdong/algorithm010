class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        un = list(range(n))

        def root(x):
            while x != un[x]:
                un[x] = un[un[x]]
                x = un[x]
            return x

        cir = n
        for i in range(n):
            for j in range(i):
                if M[i][j] == 0:
                    continue
                ri, rj = root(i), root(j)
                if ri != rj:
                    un[rj] = ri
                    cir -= 1
        return cir
